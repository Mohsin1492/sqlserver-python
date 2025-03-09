"""
Database operations (DDL) for SQL Server.
"""

from src.insert import insert_author
from src.update import update_author
from src.setup_database import setup_database
from src.procedures import call_stored_procedure

__all__ = [
    'insert_author',
    'update_author',
    'setup_database',
    'call_stored_procedure'
] 