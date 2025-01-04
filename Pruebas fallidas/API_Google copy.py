import googlemaps
import csv
import time

API_KEY = 'AIzaSyDn4CeVnXilEiMx_aVxAr_achPUwvioDkk'
gmaps = googlemaps.Client(key=API_KEY)

def search_places(location, place_type, radius=500):
    """Search for specific types of places in the given location with pagination.

    Args:
        location (str): The location to search in (e.g., Poblenou).
        place_type (str): The type of place to search for (e.g., restaurant, hotel).
        radius (int): Search radius in meters.

    Returns:
        list: A list of dictionaries containing place names and coordinates.
    """
    results = []

    # Geocode the location to get latitude and longitude
    geocode_result = gmaps.geocode(location)
    if not geocode_result:
        print("Location not found!")
        return results

    lat_lng = geocode_result[0]['geometry']['location']
    latitude, longitude = lat_lng['lat'], lat_lng['lng']

    # Initial request for places
    response = gmaps.places_nearby(
        location=(latitude, longitude),
        radius=radius,
        type=place_type  # Try with type first
    )

    if not response.get('results'):  # Fallback to keyword if no results are returned
        print(f"No results found using type '{place_type}', falling back to keyword search...")
        response = gmaps.places_nearby(
            location=(latitude, longitude),
            radius=radius,
            keyword=place_type  # Use keyword for a broader search
        )

    results.extend(process_places(response))

    # Handle pagination
    while 'next_page_token' in response:
        next_page_token = response['next_page_token']
        time.sleep(2)  # Delay required by the API
        response = gmaps.places_nearby(page_token=next_page_token)
        results.extend(process_places(response))

    return results

def process_places(response):
    """Process places from the API response."""
    return [
        {
            "name": place.get('name'),
            "latitude": place['geometry']['location']['lat'],
            "longitude": place['geometry']['location']['lng']
        }
        for place in response.get('results', [])
    ]

def save_to_csv(data, filename):
    """Save place data to a CSV file.

    Args:
        data (list): List of place dictionaries.
        filename (str): Name of the CSV file.
    """
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "latitude", "longitude"])
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    # Inputs from the user
    location = input("Enter the location (e.g., Poblenou, Barcelona): ")
    place_type = input("Enter the type of place (e.g., restaurant, hotel, cafe): ")
    radius = int(input("Enter the search radius in meters (e.g., 1000): "))

    # Fetch places
    places = search_places(location, place_type, radius)

    if places:
        print(f"{place_type.capitalize()}s found in {location}:")
        for idx, place in enumerate(places, start=1):
            print(f"{idx}. {place['name']} (Lat: {place['latitude']}, Lng: {place['longitude']})")
        
        # Save to CSV file
        filename = f"{place_type}_{location.replace(', ', '_').replace(' ', '_')}.csv"
        save_to_csv(places, filename)
        print(f"{place_type.capitalize()}s saved to '{filename}'.")
    else:
        print(f"No {place_type}s found in {location}.")
