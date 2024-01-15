```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from utils import log_error

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return "<User(name='%s', email='%s')>" % (self.name, self.email)

try:
    Base.metadata.create_all(bind=engine)
except Exception as e:
    log_error('backend/models.py', str(e))
```