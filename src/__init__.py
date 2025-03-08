"""
Database operations (DDL) for SQL Server.
"""

from src.insert import insert_author
from src.setup_database import setup_database

__all__ = [
    'insert_author',
    'setup_database'
] 