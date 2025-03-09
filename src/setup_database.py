import logging
from utils.connect import create_connection
from src.config.config import SQL_CREATE_AUTHOR_TABLE

def setup_database():
    """Create the necessary database tables if they don't exist"""
    conn = create_connection()
    if not conn:
        logging.error("Failed to connect to database for setup")
        return False
    
    cursor = None
    try:
        cursor = conn.cursor()
        
        # Create Authors table
        cursor.execute(SQL_CREATE_AUTHOR_TABLE)
        
        conn.commit()
        logging.info("Database schema setup completed successfully")
        return True
    except Exception as e:
        logging.error(f"Database setup error: {e}")
        if conn:
            conn.rollback()
        return False
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()