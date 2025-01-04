from xml.etree import ElementTree as ET
import csv

def parse_kml_to_csv(kml_file, csv_file):
    # Parse the KML file
    tree = ET.parse(kml_file)
    root = tree.getroot()

    # Define namespaces
    namespaces = {"kml": "http://www.opengis.net/kml/2.2"}

    # Find all placemarks
    placemarks = root.findall(".//kml:Placemark", namespaces)

    # Extract data
    data = []
    for placemark in placemarks:
        name = placemark.find("kml:name", namespaces).text
        point = placemark.find(".//kml:Point/kml:coordinates", namespaces)
        if point is not None:
            coordinates = point.text.strip().split(",")
            longitude, latitude = coordinates[0], coordinates[1]
            data.append([name, latitude, longitude])

    # Save to CSV
    with open(csv_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Latitude", "Longitude"])
        writer.writerows(data)

# Example usage
kml_file = "output.kml"
csv_file = "MUNS2.csv"
parse_kml_to_csv(kml_file, csv_file)
print(f"Data saved to {csv_file}")
