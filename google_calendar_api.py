```python
import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# Load environment variables
GOOGLE_CALENDAR_API_KEY = os.getenv('GOOGLE_CALENDAR_API_KEY')

# Create credentials object
credentials = Credentials.from_service_account_info(GOOGLE_CALENDAR_API_KEY)

# Build the service
service = build('calendar', 'v3', credentials=credentials)

def create_event(user_email, start_time, end_time, summary, description, location=None):
    event = {
        'summary': summary,
        'description': description,
        'start': {
            'dateTime': start_time,
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': end_time,
            'timeZone': 'America/Los_Angeles',
        },
        'attendees': [
            {'email': user_email},
        ],
    }

    if location:
        event['location'] = location

    created_event = service.events().insert(calendarId='primary', body=event).execute()

    return created_event['id']

def delete_event(event_id):
    service.events().delete(calendarId='primary', eventId=event_id).execute()

def update_event(event_id, start_time=None, end_time=None, summary=None, description=None, location=None):
    event = service.events().get(calendarId='primary', eventId=event_id).execute()

    if start_time:
        event['start']['dateTime'] = start_time
    if end_time:
        event['end']['dateTime'] = end_time
    if summary:
        event['summary'] = summary
    if description:
        event['description'] = description
    if location:
        event['location'] = location

    updated_event = service.events().update(calendarId='primary', eventId=event_id, body=event).execute()

    return updated_event['id']

def get_event(event_id):
    event = service.events().get(calendarId='primary', eventId=event_id).execute()
    return event
```