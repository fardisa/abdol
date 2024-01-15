```python
import os
import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    db_file = os.path.join(os.path.dirname(__file__), 'ai_chatbot.db')
    
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)

    if conn:
        return conn

def close_connection(conn):
    conn.close()

def execute_sql_file(conn, filename):
    file = open(filename, 'r')
    sql = file.read()
    cur = conn.cursor()
    cur.executescript(sql)

def setup_database():
    conn = create_connection()
    execute_sql_file(conn, 'database_schema.sql')
    execute_sql_file(conn, 'dummy_data.sql')
    close_connection(conn)

if __name__ == '__main__':
    setup_database()
```