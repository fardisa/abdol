```python
import os
import googlemaps

# Load Google Maps API key from environment variables
GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')

# Initialize Google Maps client
gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)

def get_location_details(location):
    """
    Function to get detailed information about a location using Google Maps API.
    """
    geocode_result = gmaps.geocode(location)
    return geocode_result

def get_directions(origin, destination):
    """
    Function to get directions from origin to destination using Google Maps API.
    """
    directions_result = gmaps.directions(origin, destination)
    return directions_result

def create_location_link(location):
    """
    Function to create a Google Maps link for a given location.
    """
    location_details = get_location_details(location)
    if location_details:
        location_link = "https://www.google.com/maps/place/?q=place_id:" + location_details[0]['place_id']
        return location_link
    else:
        return None
```