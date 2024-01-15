```python
from enum import Enum

class UserRole(Enum):
    SEEKER = 1
    PROVIDER = 2
    SUPERADMIN = 3

def is_provider(user_role):
    return user_role == UserRole.PROVIDER

def is_seeker(user_role):
    return user_role == UserRole.SEEKER

def is_superadmin(user_role):
    return user_role == UserRole.SUPERADMIN

def set_role(user, role):
    if role not in UserRole:
        raise ValueError("Invalid user role")
    user.role = role

def get_role(user):
    return user.role
```