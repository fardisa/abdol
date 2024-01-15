```python
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_secret(secret_name):
    """Retrieve secret from environment variables"""
    try:
        return os.getenv(secret_name)
    except KeyError:
        print(f"Unable to find {secret_name} in environment variables.")
        return None

def set_secret(secret_name, secret_value):
    """Set secret in environment variables"""
    os.environ[secret_name] = secret_value

def delete_secret(secret_name):
    """Delete secret from environment variables"""
    if secret_name in os.environ:
        del os.environ[secret_name]
    else:
        print(f"Unable to find {secret_name} in environment variables.")

def list_secrets():
    """List all secrets in environment variables"""
    return {key: value for key, value in os.environ.items() if 'SECRET' in key}
```