import logging
import sys
from utils.connect import create_connection
from src.setup_database import setup_database
from src.insert import insert_author
from src.update import update_author
from src.procedures import call_stored_procedure
from src.config.config import SQL_SELECT_ALL_AUTHORS

# Configure logging
logging.basicConfig(
    stream=sys.stdout, 
    encoding='utf-8', 
    format='%(levelname)s:%(message)s',
    level=logging.INFO
)

def main():
    # Set up the database schema first
    if not setup_database():
        logging.error("Database setup failed, cannot proceed")
        return
    
    # Insert a sample author
    author_id = insert_author("John", "Doe", "1970-01-01")
    if author_id:
        logging.info(f"Successfully inserted author with ID: {author_id}")
    else:
        logging.error("Failed to insert author")
        return
    
    # Update the author
    update_author(1, "Jane", "Smith", "1981-01-01")
    
    # Display all authors in the database
    display_authors()

    # Call the stored procedure
    result = call_stored_procedure("GetAuthorById", 1)
    logging.info(f"Stored procedure result: {result}")  

def display_authors():
    """Query and display all authors in the database"""
    conn = create_connection()
    if not conn:
        logging.error("Failed to connect to database for querying authors")
        return
    
    cursor = None
    try:
        cursor = conn.cursor()
        cursor.execute(SQL_SELECT_ALL_AUTHORS)
        authors = cursor.fetchall()
        
        if authors:
            logging.info(f"Found {len(authors)} authors in database:")
            for author in authors:
                logging.info(f"  ID: {author[0]}, Name: {author[1]} {author[2]}, Birth Date: {author[3]}")
        else:
            logging.info("No authors found in database")
    except Exception as e:
        logging.error(f"Error querying authors: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    main()