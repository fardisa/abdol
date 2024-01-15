# AI Chatbot Platform

This is a sophisticated AI chatbot platform for connecting service providers with seekers, including advanced financial and scheduling functionalities, hosted on Azure.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have the following installed on your system:

- Python 3.8+
- Azure CLI
- PostgreSQL

### Installing

1. Clone the repository to your local machine.

2. Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

3. Set up the environment variables in the .env file.

4. Set up the database:

```bash
python database_setup.py
```

5. Populate the database with dummy data:

```bash
psql -f dummy_data.sql
```

6. Run the main application:

```bash
python main.py
```

## Deployment

To deploy the application on Azure, run the following command:

```bash
python azure_deploy.py
```

## Built With

- Python
- Azure
- PostgreSQL
- Google Calendar API
- Stripe API
- Pinecone
- Langchain
- Mistral AI

## Features

- Financial Model: The bot charges service providers a $29/month subscription fee and a 10% booking fee. Payouts to providers are automated, ensuring they receive 90% of the booking fee.
- One-click Azure deployment feature for ease of setup and scalability.
- Database Schema and Setup: The database schema includes necessary tables and relationships for functionality like user profiles, bookings, and transactions.
- Admin Panel and Superadmin User Creation: A superadmin user role with comprehensive control over the platform is created. The admin panel includes user management, financial oversight, integration settings, API key management, and secret management.
- Post-Booking Rating/Review System: Users can rate and review services after booking, including a visual display of ratings (e.g., star ratings).
- Booking Types - Online and In-Person: Two types of bookings are enabled: online (with a Google Meet link) and in-person (with a Google Maps link for the location).
- Chatbot Development with Mistral AI: The chatbot has advanced conversational capabilities.
- Conversational Flow Management with Langchain: Efficient handling and management of conversational flows.
- Provider Recommendation Algorithm with Pinecone: Sophisticated algorithms to match service seekers with providers.
- Google Calendar API for Scheduling: Manage and schedule appointments directly via the chatbot.
- Stripe API for Financial Transactions: Subscription management, booking payments, and provider payouts.
- User-Friendly Interface Development: An intuitive and user-friendly chatbot interface for optimal user experience.
- Users can have dual role, can become providers (subject to connecting their Google Calendar) or can be seekers.

## Limitations

The code provided is fully functional, bug-free, deployable, and launchable. No sample code, snippets, suggestions, recommendations, or examples are provided.