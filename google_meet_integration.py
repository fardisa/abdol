```python
import os
import google.auth
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these SCOPES, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.events']

def create_google_meet_link(booking_id):
    """Shows basic usage of the Google Calendar API.
    Creates a Google Calendar event with a Google Meet link.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json')
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    event = {
      'summary': 'Booking ID: {}'.format(booking_id),
      'location': 'Online',
      'description': 'Online meeting for booking ID: {}'.format(booking_id),
      'start': {
        'dateTime': '2022-01-01T09:00:00-07:00',
        'timeZone': 'America/Los_Angeles',
      },
      'end': {
        'dateTime': '2022-01-01T17:00:00-07:00',
        'timeZone': 'America/Los_Angeles',
      },
      'conferenceData': {
        'createRequest': {
          'requestId': 'sample123',  # TODO: Update with unique identifier
          'conferenceSolutionKey': {
            'type': 'hangoutsMeet'
          }
        }
      },
      'attendees': [
        {'email': 'example@example.com'},  # TODO: Update with provider email
      ],
      'reminders': {
        'useDefault': False,
        'overrides': [
          {'method': 'email', 'minutes': 24 * 60},
          {'method': 'popup', 'minutes': 10},
        ],
      },
    }

    event = service.events().insert(calendarId='primary', body=event, conferenceDataVersion=1).execute()
    print('Event created: %s' % (event.get('htmlLink')))

    return event.get('hangoutLink')
```