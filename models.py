```python
from peewee import *

db = SqliteDatabase('database.db')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    username = CharField(unique=True)
    password = CharField()

class Post(BaseModel):
    user = ForeignKeyField(User, backref='posts')
    content = TextField()

def initialize():
    db.connect()
    db.create_tables([User, Post])

def close_connection():
    db.close()

if __name__ == "__main__":
    initialize()
```