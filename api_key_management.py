```python
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define API keys
GOOGLE_CALENDAR_API_KEY = os.getenv('GOOGLE_CALENDAR_API_KEY')
STRIPE_API_KEY = os.getenv('STRIPE_API_KEY')
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
LANGCHAIN_API_KEY = os.getenv('LANGCHAIN_API_KEY')
MISTRAL_AI_API_KEY = os.getenv('MISTRAL_AI_API_KEY')
AZURE_API_KEY = os.getenv('AZURE_API_KEY')

def get_api_key(service_name):
    """
    Function to get the API key for a given service
    """
    if service_name == 'google_calendar':
        return GOOGLE_CALENDAR_API_KEY
    elif service_name == 'stripe':
        return STRIPE_API_KEY
    elif service_name == 'pinecone':
        return PINECONE_API_KEY
    elif service_name == 'langchain':
        return LANGCHAIN_API_KEY
    elif service_name == 'mistral_ai':
        return MISTRAL_AI_API_KEY
    elif service_name == 'azure':
        return AZURE_API_KEY
    else:
        return None

def update_api_key(service_name, new_key):
    """
    Function to update the API key for a given service
    """
    if service_name == 'google_calendar':
        os.environ['GOOGLE_CALENDAR_API_KEY'] = new_key
    elif service_name == 'stripe':
        os.environ['STRIPE_API_KEY'] = new_key
    elif service_name == 'pinecone':
        os.environ['PINECONE_API_KEY'] = new_key
    elif service_name == 'langchain':
        os.environ['LANGCHAIN_API_KEY'] = new_key
    elif service_name == 'mistral_ai':
        os.environ['MISTRAL_AI_API_KEY'] = new_key
    elif service_name == 'azure':
        os.environ['AZURE_API_KEY'] = new_key
    else:
        return None
```