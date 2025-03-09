SQL_CREATE_AUTHOR_TABLE = """
-- Create Authors table if it doesn't exist
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Authors')
BEGIN
    CREATE TABLE Authors ( 
        AuthorID INT PRIMARY KEY,
        FirstName NVARCHAR(100) NOT NULL,
        LastName NVARCHAR(100) NOT NULL,
        BirthDate DATE NULL
    )
END
""" 

SQL_CREATE_STORED_PROCEDURE = """
-- Create GetAuthorById stored procedure if it doesn't exist
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
"""

SQL_INSERT_AUTHOR = """
-- Insert a new author into the Authors table
INSERT INTO Authors (AuthorID, FirstName, LastName, BirthDate)
VALUES (@AuthorID, @FirstName, @LastName, @BirthDate)
"""

SQL_UPDATE_AUTHOR = """
-- Update an existing author in the Authors table
UPDATE Authors
SET FirstName = @FirstName, LastName = @LastName, BirthDate = @BirthDate
WHERE AuthorID = @AuthorID
"""

SQL_SELECT_ALL_AUTHORS = """
-- Select all authors from the Authors table
SELECT * FROM Authors
"""

