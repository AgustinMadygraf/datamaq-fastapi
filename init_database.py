"""
Path: db_inicializer.py
"""

from src.infrastructure.sql_alchemy.database_setup import DatabaseInitializer

if __name__ == "__main__":
    initializer = DatabaseInitializer()
    initializer.initialize()
