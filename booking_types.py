```python
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

class BookingTypes:
    def __init__(self):
        self.google_maps_api_key = os.getenv('GOOGLE_MAPS_API_KEY')
        self.google_meet_api_key = os.getenv('GOOGLE_MEET_API_KEY')

    def create_online_booking(self, service_provider, service_seeker, booking_time):
        # Create a Google Meet link using Google Meet API
        # This is a placeholder, replace with actual API call
        meet_link = f"https://meet.google.com/{service_provider}-{service_seeker}-{booking_time}"
        return meet_link

    def create_in_person_booking(self, service_provider, service_seeker, booking_time, location):
        # Create a Google Maps link using Google Maps API
        # This is a placeholder, replace with actual API call
        maps_link = f"https://www.google.com/maps/search/?api=1&query={location}"
        return maps_link
```