import requests
import pandas as pd
import statistics
import folium
from folium.plugins import HeatMap
import time

def fetch_places(query, location, api_key, max_results=100):
    
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
            
            
            next_page_token = response.json().get('next_page_token')
            if not next_page_token or len(places) >= max_results:
                break
            
           
            params["pagetoken"] = next_page_token
            time.sleep(2)  
        else:
            print(f"Error: {response.status_code} - {response.text}")
            break
    
    return places[:max_results]

def extract_place_details(results):
    
    places = []
    for result in results:
        name = result.get("name")
        lat = result.get("geometry", {}).get("location", {}).get("lat")
        lng = result.get("geometry", {}).get("location", {}).get("lng")
        if name and lat and lng:
            places.append({"name": name, "latitude": lat, "longitude": lng})
    return places

def save_to_csv(data, filename):
    
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

def create_heatmap(csv_file, output_file):
    data = pd.read_csv(csv_file)
    longs = data["longitude"]
    lats = data["latitude"]
    mean_long = statistics.mean(longs)
    mean_lat = statistics.mean(lats)
    map_obj = folium.Map(location=[mean_lat, mean_long], zoom_start=14.5)
    heatmap = HeatMap(
        list(zip(lats, longs)),
        min_opacity=0.2,
        radius=20,
        blur=15,
        max_zoom=1
    )
    heatmap.add_to(map_obj)
    map_obj.save(output_file)
    print(f"Heatmap saved to {output_file}")

