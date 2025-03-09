# call the stored procedure with parameters and return the result
import logging
from utils.connect import create_connection

def call_stored_procedure(procedure_name, parameters):  
    logging.basicConfig(level=logging.INFO)
    logging.info(f'Calling stored procedure: {procedure_name} with parameters: {parameters}')
    conn = create_connection()
    if conn is None:
        logging.error('Failed to connect to the SQL Server database.')
        return False
    
    try:
        cursor = conn.cursor()
        cursor.execute(f"EXEC {procedure_name}", parameters)
        result = cursor.fetchall()
        logging.info(f'Stored procedure {procedure_name} executed successfully.')
        return result
    except Exception as e:
        logging.error(f'Error calling stored procedure: {e}')
        return False
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    call_stored_procedure("GetAuthorById", 1)
