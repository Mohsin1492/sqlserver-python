import logging
from utils.connect import create_connection

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
        cursor.execute("""
        IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Authors')
        BEGIN
            CREATE TABLE Authors (
                AuthorID INT IDENTITY(1,1) PRIMARY KEY,
                FirstName NVARCHAR(100) NOT NULL,
                LastName NVARCHAR(100) NOT NULL,
                BirthDate DATE NULL
            )
        END
        """)

        # Check if the stored procedure already exists, if not create it
        cursor.execute("""
        IF NOT EXISTS (SELECT * FROM sys.procedures WHERE name = 'GetAuthorById')
        BEGIN
            EXEC('
                CREATE PROCEDURE GetAuthorById
                    @AuthorID INT
                AS
                BEGIN
                    SELECT * FROM Authors WHERE AuthorID = @AuthorID
                END
            ')
        END
        """)
        
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