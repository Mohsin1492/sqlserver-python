import logging
from utils.connect import create_connection

def healthcheck():
    conn = create_connection()
    if conn:
        logging.basicConfig(level=logging.INFO)
        logging.info('Connected to the SQL Server database successfully.')
        
        # Test query
        cursor = conn.cursor()
        cursor.execute("SELECT @@VERSION")
        row = cursor.fetchone()
        print(f"SQL Server version: {row[0]}")
        
        cursor.close()
        conn.close()
        return True
    else:
        logging.error('Failed to connect to the SQL Server database.')
        return False
    
if __name__ == "__main__":
    healthcheck()
