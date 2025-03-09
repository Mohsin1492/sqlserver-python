# update the author details in the database

import logging
from utils.connect import create_connection

def update_author(author_id: int, first_name: str, last_name: str, birth_date: str) -> bool:
    """
    Update an existing author in the database
    
    Args:
        author_id: ID of the author to update
        first_name: New first name
        last_name: New last name
        birth_date: New birth date in 'YYYY-MM-DD' format
        
    Returns:
        True if update successful, False otherwise
    """
    conn = create_connection()
    if not conn:
        logging.error("Failed to connect to database for author update")
        return False
    
    cursor = None
    try:
        cursor = conn.cursor()
        
        # Update the author
        cursor.execute(
            """
            UPDATE Authors 
            SET FirstName = ?, LastName = ?, BirthDate = ? 
            WHERE AuthorID = ?
            """,
            (first_name, last_name, birth_date, author_id)
        )
        
        # Check if any rows were affected
        rows_affected = cursor.rowcount
        conn.commit()
        
        if rows_affected > 0:
            logging.info(f"Author ID {author_id} updated successfully")
            return True
        else:
            logging.warning(f"No author found with ID {author_id}, nothing updated")
            return False
    except Exception as e:
        logging.error(f"Update error: {e}")
        if conn:
            conn.rollback()
        return False
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# test the update_author function
if __name__ == "__main__":
    update_author(1, 'John', 'Doe', '1990-01-01')
        
        
        
        
