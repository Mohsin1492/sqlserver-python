import os, logging
import pyodbc
from dotenv import load_dotenv


def create_connection():
    """Create a connection to SQL Server using ODBC Driver 17"""
    load_dotenv()
    
    # Create connection string with ODBC Driver 17
    conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={os.getenv('DB_SERVER')};"
        f"DATABASE={os.getenv('DB_NAME')};"
        f"UID={os.getenv('DB_USER')};"
        f"PWD={os.getenv('DB_PASSWORD')};"
        f"Trusted_Connection=no;"
    )
    
    try:
        return pyodbc.connect(conn_str)
    except Exception as e:
        logging.error(f"Connection error: {e}")
        return None 