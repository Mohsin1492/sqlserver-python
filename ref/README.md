# SQL Server Python Connection

This project demonstrates how to connect to a SQL Server database using Python with pyodbc.

## Table of Contents
- [Connection Method](#connection-method)
- [Project Structure](#project-structure)
- [Setup](#setup)
- [SQL Server User Creation](#sql-server-user-creation)
- [Running the Example](#running-the-example)
- [Troubleshooting](#troubleshooting)
- [Why pyodbc with ODBC Driver 17?](#why-pyodbc-with-odbc-driver-17)

## Connection Method

This project uses **pyodbc** with **ODBC Driver 17 for SQL Server**, which is the most reliable approach for connecting to SQL Server from Python on Windows.

## Project Structure

```
├── main.py                # Main application entry point
├── requirements.txt       # Python dependencies
├── .env                   # Database configuration (not in repo)
├── src/                   # Database operations (DDL)
│   ├── __init__.py        # Package initialization
│   ├── setup_database.py  # Database schema creation
│   ├── insert.py          # Data insertion functions
│   ├── update.py          # Data update functions
│   ├── procedures.py      # Stored procedure calling
│   └── ...                # Other database operations
└── utils/                 # Utility package
    ├── __init__.py        # Package initialization
    ├── connect.py         # Database connection handling
    └── healthcheck.py     # Database connectivity verification
```

## Setup

1. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

2. Configure your database connection in the `.env` file:
   ```
   DB_SERVER="localhost\\SQLEXPRESS"
   DB_NAME=master
   DB_USER=sa
   DB_PASSWORD=your_password
   ```

## SQL Server User Creation

Before running the application, you may need to create a dedicated SQL Server user with appropriate permissions. Run the following SQL commands in SQL Server Management Studio or using the `sqlcmd` utility:

```sql
USE master;

-- Create a SQL Server Login (For SQL Authentication)
GO
CREATE LOGIN svc_sqlserver WITH PASSWORD = 'YourStrongPassword123';
GO

-- Create a User in a Specific Database
GO
CREATE USER svc_sqlserver FOR LOGIN svc_sqlserver;
GO

--===================
-- Grant Permissions
--===================

-- Give Read Access (SELECT on all tables):
ALTER ROLE db_datareader ADD MEMBER svc_sqlserver;

-- Give Write Access (INSERT, UPDATE, DELETE):
ALTER ROLE db_datawriter ADD MEMBER svc_sqlserver;

-- Give Full Control (including schema changes):
ALTER ROLE db_owner ADD MEMBER svc_sqlserver;

--======================
-- Verify User Creation
--======================

-- Run the following query to check if the user exists:
SELECT * FROM sys.database_principals WHERE type = 'S';
```

> **Note**: Replace 'YourStrongPassword123' with a secure password following your organization's password policy.

## Running the Example

Run the connection example with:
```
python main.py
```

This will:
1. Create the necessary database schema and stored procedures
2. Insert a sample author record
3. Update an existing author record
4. Call a stored procedure to retrieve an author by ID
5. Display all authors in the database

## Troubleshooting

If you're having issues connecting to SQL Server:

1. **ODBC Driver**: Make sure ODBC Driver 17 for SQL Server is installed on your system

2. **SQL Server Browser Service**: Make sure the SQL Server Browser service is running (requires admin privileges):
   ```
   net start sqlbrowser
   ```

3. **TCP/IP Protocol**: Ensure TCP/IP protocol is enabled in SQL Server Configuration Manager

4. **SQL Authentication**: Verify SQL Server is configured to allow SQL authentication (not just Windows auth)

5. **Test with sqlcmd**: Verify your SQL Server is accessible with the command-line tool:
   ```
   sqlcmd -S "localhost\SQLEXPRESS" -U sa -P "your_password" -Q "SELECT @@VERSION"
   ```

6. **Database Permissions**: Ensure the user has appropriate permissions as outlined in the [SQL Server User Creation](#sql-server-user-creation) section

## Why pyodbc with ODBC Driver 17?

The ODBC Driver 17 for SQL Server is Microsoft's recommended driver for SQL Server connectivity. It provides:

- Better performance and stability
- Support for modern SQL Server features
- Proper handling of named instances
- Active maintenance and updates from Microsoft

When working with SQL Server on Windows, this approach offers the most reliable connection experience. 