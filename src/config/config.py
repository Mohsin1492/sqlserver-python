SQL_CREATE_AUTHOR_TABLE = """
-- Create Authors table if it doesn't exist
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'Authors')
BEGIN
    CREATE TABLE Authors ( 
        AuthorID INT IDENTITY PRIMARY KEY,
        FirstName NVARCHAR(100) NOT NULL,
        LastName NVARCHAR(100) NOT NULL,
        BirthDate DATE NULL
    )
END
"""