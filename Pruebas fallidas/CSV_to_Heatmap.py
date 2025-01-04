# Import relevant packages
import pandas
import folium
from folium.plugins import HeatMap
import statistics

# Read in CSV file containing location data
data = pandas.read_csv("restaurants_clot.csv")

# Extract longitude and latitude
longs = data["longitude"]
lats = data["latitude"]

# Calculate mean longitude and latitude values for centering the map
meanLong = statistics.mean(longs)
meanLat = statistics.mean(lats)

# Create a base map object
mapObj = folium.Map(location=[meanLat, meanLong], zoom_start=14.5)

# Create a heatmap layer
heatmap = HeatMap(
    list(zip(lats, longs)),
    min_opacity=0.2,
    radius=35,  # Adjust radius for better visualization
    blur=20,    # Adjust blur for better visualization
    max_zoom=1
)

# Add heatmap layer to base map
heatmap.add_to(mapObj)

# Save the map to an HTML file and display it
mapObj.save("restaurants_clot.html")
print("CAfe saved as cafe.html")

