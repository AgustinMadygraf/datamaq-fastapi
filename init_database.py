"""
Path: db_inicializer.py
"""

from tools.database_setup import DatabaseInitializer

if __name__ == "__main__":
    initializer = DatabaseInitializer()
    initializer.initialize()
