import os, sys
from PyQt5.QtCore import QTimer
from scipy.datasets import face

    # path to look for files
path = "osm_project.qgz"
    # set path
dirs = os.listdir( path )
    # array for storing layer_names
layer_list = []
    # variable for further processing
count = 0
    #look for files inpath
for file in dirs:
    	# search for ".gpkg" files 
    if file.endswith(".qgz"):
    		#add vectorlayers
        vlayer = face.addVectorLayer(path + file, "Layername", "ogr")
        layer_list.append(vlayer.name())