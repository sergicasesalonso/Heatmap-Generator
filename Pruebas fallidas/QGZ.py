from qgis.core import (
    QgsApplication,
    QgsProject,
    QgsRasterLayer,
    QgsCoordinateReferenceSystem,
    QgsVectorLayer,
    QgsFeature,
    QgsGeometry,
    QgsPointXY,
    QgsField
)
from qgis.gui import QgsMapCanvas, QgsLayerTreeMapCanvasBridge
from qgis.PyQt.QtCore import QVariant
import csv
import os

# Initialize the QGIS Application
QgsApplication.setPrefixPath("C:/Program Files/QGIS 3.34.13/apps/qgis-ltr", True)
qgs = QgsApplication([], False)
qgs.initQgis()

# Create a QGIS project and map canvas
project = QgsProject.instance()
canvas = QgsMapCanvas()

def add_osm_basemap():
    """Function to add the OSM Standard Basemap"""
    osm_url = "type=xyz&url=https://a.tile.openstreetmap.org/{z}/{x}/{y}.png"
    osm_layer = QgsRasterLayer(osm_url, "OSM Standard", "wms")

    if not osm_layer.isValid():
        print("Failed to load the OSM Standard layer.")
        return False

    project.addMapLayer(osm_layer)
    print("OSM Standard Basemap added successfully.")
    return True

def add_points_from_csv(csv_file_path):
    """Function to add points from a CSV file to the project."""
    # Define the vector layer
    vl = QgsVectorLayer("Point?crs=EPSG:4326", "CSV Points", "memory")
    pr = vl.dataProvider()

    # Add fields for name and coordinates
    pr.addAttributes([
        QgsField("name", QVariant.String),
        QgsField("latitude", QVariant.Double),
        QgsField("longitude", QVariant.Double)
    ])
    vl.updateFields()

    # Read the CSV and add points
    try:
        with open(csv_file_path, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            features = []
            for row in reader:
                # Debug: Check the content of the row
                print(f"Processing row: {row}")

                # Extract data
                name = row.get("name")
                latitude = row.get("latitude")
                longitude = row.get("longitude")

                if not name or not latitude or not longitude:
                    print(f"Skipping row due to missing values: {row}")
                    continue

                try:
                    latitude = float(latitude)
                    longitude = float(longitude)
                except ValueError as e:
                    print(f"Error converting coordinates to float: {e}")
                    continue

                # Create a feature
                feature = QgsFeature()
                feature.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(longitude, latitude)))
                feature.setAttributes([name, latitude, longitude])
                features.append(feature)

            # Debug: Check the number of features created
            print(f"Number of features created: {len(features)}")

            # Add features to the layer
            pr.addFeatures(features)

    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return

    vl.updateExtents()
    project.addMapLayer(vl)
    print(f"Points from {csv_file_path} added successfully.")

# Add the OSM Basemap to the project
if add_osm_basemap():
    # Link the map canvas to the project's layer tree
    root = project.layerTreeRoot()
    bridge = QgsLayerTreeMapCanvasBridge(root, canvas)

    # Set the CRS and configure the canvas
    canvas.setDestinationCrs(QgsCoordinateReferenceSystem("EPSG:3857"))  # Web Mercator
    canvas.resize(800, 600)
    canvas.show()

# Path to the CSV file
csv_file_path = "restaurants_poblenou.csv"  # Update this path to your CSV file

if os.path.exists(csv_file_path):
    add_points_from_csv(csv_file_path)
else:
    print(f"CSV file not found: {csv_file_path}")

# Save the project
project_file = "osm_project_with_points.qgz"
project.write(project_file)
print(f"Project saved to {project_file}")

# Exit QGIS
qgs.exitQgis()
