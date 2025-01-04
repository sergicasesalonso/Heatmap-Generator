from qgis.core import *


# Supply path to QGIS install location
QgsApplication.setPrefixPath("C:/Program Files/QGIS 3.34.13/apps/qgis-ltr", True)

# Create a reference to the QgsApplication
qgs = QgsApplication([], False)

# Initialize QGIS application
qgs.initQgis()

# Define the path to the CSV file
path_to_csv = r"C:\Users\sergi\OneDrive\Escriptori\HeatMaps\restaurants_poblenou.csv?xField=longitude&yField=latitude&crs=EPSG:4326"
layer = QgsVectorLayer(path_to_csv, baseName="CSV file", providerLib="delimitedtext")

# Check if the layer is valid
if not layer.isValid():
    print("Layer failed to load!")
else:
    print("Layer loaded successfully!")

# Specify the output path for the GeoPackage
output_gpkg_path = r"C:\Users\sergi\OneDrive\Escriptori\HeatMaps\restaurants_poblenou.gpkg"

# Create options for saving the layer
options = QgsVectorFileWriter.SaveVectorOptions()
options.driverName = "GPKG"
options.fileEncoding = "UTF-8"

# Export the layer to GeoPackage
error = QgsVectorFileWriter.writeAsVectorFormatV3(layer, output_gpkg_path, QgsCoordinateTransformContext(), options)

# Check for errors during export
if error[0] != QgsVectorFileWriter.NoError:
    print(f"Error occurred during export: {error[0]}")
else:
    print(f"Layer successfully exported to {output_gpkg_path}")

# Close QGIS application
qgs.exitQgis()


