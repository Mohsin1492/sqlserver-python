import logging
from utils.connect import create_connection

def call_stored_procedure(procedure_name: str, *args):
    """
    Call a SQL Server stored procedure with provided arguments and return the result
    
    Args:
        procedure_name: Name of the stored procedure to call
        *args: Arguments to pass to the stored procedure
        
    Returns:
        List of results from the stored procedure or None if error
    """
    conn = create_connection()
    if not conn:
        logging.error(f"Failed to connect to database for calling procedure {procedure_name}")
        return None
    
    cursor = None
    try:
        cursor = conn.cursor()
        
        # Prepare the EXEC statement with parameter placeholders
        param_placeholders = ', '.join(['?' for _ in args])
        sql = f"EXEC {procedure_name} {param_placeholders}"
        
        # Execute the procedure
        cursor.execute(sql, args)
        
        # Fetch results if any
        results = []
        try:
            # Try to fetch all rows
            rows = cursor.fetchall()
            if rows:
                # Get column names
                columns = [column[0] for column in cursor.description]
                
                # Create a list of dictionaries for each row
                for row in rows:
                    result_dict = {}
                    for i, value in enumerate(row):
                        result_dict[columns[i]] = value
                    results.append(result_dict)
                    
                return results
        except Exception as e:
            # If no results to fetch (e.g., for INSERT, UPDATE, DELETE procedures)
            return True
            
        return results
    except Exception as e:
        logging.error(f"Error calling stored procedure {procedure_name}: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close() 