# pylint disable
"""
Path: tools/db_inicializer.py
"""

import os
from sqlalchemy import create_engine, text, inspect
from sqlalchemy.exc import SQLAlchemyError

from src.shared.config import get_mysql_config
from src.infrastructure.sql_alchemy.models import Base

class DatabaseInitializer:
    " Clase para inicializar la base de datos MySQL "
    def __init__(self):
        self.cfg = get_mysql_config()
        self.db_url = f"mysql+pymysql://{self.cfg['user']}:{self.cfg['password']}@{self.cfg['host']}:{self.cfg['port']}/{self.cfg['database']}"
        self.engine = None

    def database_exists(self):
        " Verificar si la base de datos existe "
        try:
            url_no_db = f"mysql+pymysql://{self.cfg['user']}:{self.cfg['password']}@{self.cfg['host']}:{self.cfg['port']}/"
            engine = create_engine(url_no_db)
            with engine.connect() as conn:
                result = conn.execute(
                    text("SHOW DATABASES LIKE :db"), {"db": self.cfg['database']}
                )
                return result.first() is not None
        except SQLAlchemyError as e:
            print(f"Error verificando existencia de la base de datos: {e}")
            return False

    def create_database(self):
        " Crear la base de datos si no existe "
        try:
            url_no_db = f"mysql+pymysql://{self.cfg['user']}:{self.cfg['password']}@{self.cfg['host']}:{self.cfg['port']}/"
            engine = create_engine(url_no_db)
            with engine.connect() as conn:
                conn.execute(text(f"CREATE DATABASE IF NOT EXISTS `{self.cfg['database']}` DEFAULT CHARACTER SET utf8mb4"))
                print(f"Base de datos '{self.cfg['database']}' creada (si no existía).")
        except SQLAlchemyError as e:
            print(f"Error creando la base de datos: {e}")

    def connect(self):
        " Conectar a la base de datos "
        try:
            self.engine = create_engine(self.db_url, echo=True)
        except SQLAlchemyError as e:
            print(f"Error conectando a la base de datos: {e}")

    def tables_exist(self):
        " Verificar si las tablas existen "
        inspector = None
        try:
            inspector = inspect(self.engine)
            tables = inspector.get_table_names()
            return bool(tables)
        except SQLAlchemyError as e:
            print(f"Error al inspeccionar la base de datos: {e}")
            return False

    def create_tables(self):
        " Crear las tablas si no existen "
        try:
            Base.metadata.create_all(self.engine)
            print("Tablas creadas (si no existían).")
        except SQLAlchemyError as e:
            print(f"Error creando las tablas: {e}")
            return
        # Ejecutar el SQL de intervalproduction.sql
        try:
            sql_path = os.path.join(os.path.dirname(__file__), '../database/intervalproduction.sql')
            sql_path = os.path.abspath(sql_path)
            if os.path.exists(sql_path):
                with open(sql_path, encoding='utf-8') as f:
                    sql_commands = f.read()
                with self.engine.begin() as conn:
                    for statement in sql_commands.split(';'):
                        stmt = statement.strip()
                        if stmt:
                            try:
                                conn.execute(text(stmt))
                            except SQLAlchemyError as e:
                                print(f"Error ejecutando statement: {stmt[:50]}...\n{e}")
                print("Datos de intervalproduction.sql insertados.")
            else:
                print(f"No se encontró el archivo {sql_path}")
        except SQLAlchemyError as e:
            print(f"Error procesando intervalproduction.sql: {e}")

    def initialize(self):
        " Inicializar la base de datos y las tablas "
        print("Inicializando la base de datos...")
        try:
            if not self.database_exists():
                print("La base de datos no existe. Creando...")
                self.create_database()
            else:
                print("La base de datos ya existe.")
            self.connect()
            if not self.tables_exist():
                print("Las tablas no existen. Creando...")
                self.create_tables()
            else:
                print("Las tablas ya existen.")
            print("¡Listo!")
        except SQLAlchemyError as e:
            print(f"Error de SQLAlchemy: {e}")
