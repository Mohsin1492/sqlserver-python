import logging
from utils.connect import create_connection


def insert_author(first_name: str, last_name: str, birth_date: str) -> int | None:
    """Insert an author into the database and return the author ID"""
    
    # Connect to the database
    conn = create_connection()
    if not conn:
        return None
    
    cursor = None
    try:
        cursor = conn.cursor()
        # Insert the author
        cursor.execute(
            "INSERT INTO Authors (FirstName, LastName, BirthDate) VALUES (?, ?, ?)",
            (first_name, last_name, birth_date)
        )
        conn.commit()
        
        # Get the last inserted ID
        cursor.execute("SELECT @@IDENTITY AS ID")
        author_id = cursor.fetchone()[0]
        return author_id
    except Exception as e:
        logging.error(f"Insert error: {e}")
        if conn:
            conn.rollback()
        return None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

