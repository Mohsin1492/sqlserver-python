import logging
import sys
from utils.connect import create_connection
from src.setup_database import setup_database
from src.insert import insert_author

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
    
main()