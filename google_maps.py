import googlemaps
from geopy.geocoders import Nominatim

# Use your own Google Maps API key here
gmaps = googlemaps.Client(key='YOUR_API_KEY')

# Initialize geolocator
geolocator = Nominatim(user_agent="geoapiExercises")

def find_food_banks(zip_code):
    # Get location coordinates from zip code
    location = geolocator.geocode(zip_code)
    coordinates = f"{location.latitude}, {location.longitude}"

    # Search for food banks
    result = gmaps.places_nearby(location=coordinates, radius=5000, keyword='food bank')

    # Print the results
    for place in result['results']:
        print(place['name'], place['vicinity'])

# Test the function
find_food_banks("95112")
