import logging
from utils.connect import create_connection
from src.config.config import SQL_CREATE_AUTHOR_TABLE, SQL_CREATE_STORED_PROCEDURE

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

        # Check if the stored procedure already exists, if not create it
        cursor.execute(SQL_CREATE_STORED_PROCEDURE)
        
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

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')
    setup_database() 