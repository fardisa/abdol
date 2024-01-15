import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Google Calendar API
GOOGLE_CALENDAR_API_KEY = os.getenv('GOOGLE_CALENDAR_API_KEY')

# Stripe API
STRIPE_API_KEY = os.getenv('STRIPE_API_KEY')

# Pinecone API
PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')

# Langchain API
LANGCHAIN_API_KEY = os.getenv('LANGCHAIN_API_KEY')

# Mistral AI API
MISTRAL_AI_API_KEY = os.getenv('MISTRAL_AI_API_KEY')

# Google Meet API
GOOGLE_MEET_API_KEY = os.getenv('GOOGLE_MEET_API_KEY')

# Google Maps API
GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')

# Azure Deployment Settings
AZURE_SUBSCRIPTION_ID = os.getenv('AZURE_SUBSCRIPTION_ID')
AZURE_RESOURCE_GROUP = os.getenv('AZURE_RESOURCE_GROUP')
AZURE_STORAGE_ACCOUNT = os.getenv('AZURE_STORAGE_ACCOUNT')
AZURE_APP_SERVICE_PLAN = os.getenv('AZURE_APP_SERVICE_PLAN')
AZURE_APP_NAME = os.getenv('AZURE_APP_NAME')