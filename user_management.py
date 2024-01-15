```python
import os
import psycopg2
from psycopg2 import sql

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Database connection parameters
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

# Connect to the database
conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)

# Create a cursor object
cur = conn.cursor()

def create_user(user_data):
    """Create a new user in the database."""
    query = sql.SQL(
        "INSERT INTO users (username, email, password, role) VALUES (%s, %s, %s, %s)"
    )
    cur.execute(query, (user_data['username'], user_data['email'], user_data['password'], user_data['role']))
    conn.commit()

def update_user(user_id, user_data):
    """Update a user's information in the database."""
    query = sql.SQL(
        "UPDATE users SET username = %s, email = %s, password = %s, role = %s WHERE id = %s"
    )
    cur.execute(query, (user_data['username'], user_data['email'], user_data['password'], user_data['role'], user_id))
    conn.commit()

def delete_user(user_id):
    """Delete a user from the database."""
    query = sql.SQL("DELETE FROM users WHERE id = %s")
    cur.execute(query, (user_id,))
    conn.commit()

def get_user(user_id):
    """Retrieve a user's information from the database."""
    query = sql.SQL("SELECT * FROM users WHERE id = %s")
    cur.execute(query, (user_id,))
    user = cur.fetchone()
    return user

def get_all_users():
    """Retrieve all users' information from the database."""
    query = sql.SQL("SELECT * FROM users")
    cur.execute(query)
    users = cur.fetchall()
    return users
```