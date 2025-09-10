"""
SQLAlchemy session factory para inyección de dependencias
Path: src/infrastructure/sql_alchemy/session_factory.py
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from src.shared.config import get_mysql_config

cfg = get_mysql_config()
DATABASE_URL = f"mysql+pymysql://{cfg['user']}:{cfg['password']}@{cfg['host']}:{cfg['port']}/{cfg['database']}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session() -> Session:
    """Obtiene una nueva sesión de base de datos"""
    return SessionLocal()
