```python
import sqlite3
from sqlite3 import Error
from utils import log_error, log_change

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect(':memory:') # create a database connection to a SQLite database in RAM
        log_change("Database connection created successfully")
    except Error as e:
        log_error(e)

    return conn

def close_connection(conn):
    try:
        conn.close()
        log_change("Database connection closed successfully")
    except Error as e:
        log_error(e)

def execute_query(conn, query):
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        log_change(f"Query executed successfully: {query}")
    except Error as e:
        log_error(e)

def main():
    conn = create_connection()
    # Add your queries here
    # execute_query(conn, YOUR_QUERY)
    close_connection(conn)

if __name__ == '__main__':
    main()
```