```python
import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect(':memory:')       
        print(sqlite3.version)
    except Error as e:
        print(e)
    if conn:
        return conn

def close_connection(conn):
    conn.close()

def create_review_table(conn):
    try:
        sql_create_reviews_table = """ CREATE TABLE IF NOT EXISTS reviews (
                                            id integer PRIMARY KEY,
                                            user_id integer NOT NULL,
                                            provider_id integer NOT NULL,
                                            booking_id integer NOT NULL,
                                            rating integer NOT NULL,
                                            review text NOT NULL,
                                            date text NOT NULL
                                        ); """
        c = conn.cursor()
        c.execute(sql_create_reviews_table)
    except Error as e:
        print(e)

def create_review(conn, review):
    sql = ''' INSERT INTO reviews(user_id,provider_id,booking_id,rating,review,date)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, review)
    return cur.lastrowid

def get_reviews_by_provider_id(conn, provider_id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM reviews WHERE provider_id=?", (provider_id,))

    rows = cur.fetchall()

    for row in rows:
        print(row)

def main():
    conn = create_connection()
    if conn is not None:
        create_review_table(conn)
        review = (1, 2, 3, 5, 'Great service!', '2022-01-01')
        create_review(conn, review)
        get_reviews_by_provider_id(conn, 2)
    else:
        print("Error! cannot create the database connection.")
    close_connection(conn)

if __name__ == '__main__':
    main()
```