import requests
import pandas as pd

def fetch_places(query, location, api_key, max_results=100):
    """
    Fetches places from Google Places API with support for pagination.
    """
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        "query": f"{query} in {location}",
        "key": api_key
    }
    places = []
    while len(places) < max_results:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            results = response.json().get('results', [])
            places.extend(results)
            
            # Stop if no next_page_token or we've reached the max results
            next_page_token = response.json().get('next_page_token')
            if not next_page_token or len(places) >= max_results:
                break
            
            # Add next_page_token to params and wait a short time before continuing
            params["pagetoken"] = next_page_token
            import time
            time.sleep(2)  # Google requires a short delay before using the token
        else:
            print(f"Error: {response.status_code} - {response.text}")
            break
    
    return places[:max_results]

def extract_place_details(results):
    """
    Extracts name, latitude, and longitude from API results.
    """
    places = []
    for result in results:
        name = result.get("name")
        lat = result.get("geometry", {}).get("location", {}).get("lat")
        lng = result.get("geometry", {}).get("location", {}).get("lng")
        if name and lat and lng:
            places.append({"name": name, "latitude": lat, "longitude": lng})
    return places

def save_to_csv(data, filename):
    """
    Saves place details to a CSV file.
    """
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    # Input
    query = input("Enter the type of place (e.g., 'gym'): ")
    location = input("Enter the location (e.g., 'Barcelona'): ")
    api_key = 'AIzaSyDn4CeVnXilEiMx_aVxAr_achPUwvioDkk'
    
    # Fetch places
    max_results = int(input("Enter the maximum number of results (e.g., 100): "))
    results = fetch_places(query, location, api_key, max_results)
    
    # Extract details
    places = extract_place_details(results)
    
    # Save to CSV
    if places:
        save_to_csv(places, "restaurants_clot.csv")
    else:
        print("No places found.")
