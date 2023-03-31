## code innterpretation
# 1.This code calls the python interface in ArcGIS to achieve the following goal: 
#   according to the existing station latitude and longitude, 
#   based on the regional precipitation tiff data, 
#   extract the precipitation data of the corresponding station
# 2.The method used in ArcGIS is: Extract Multiple Values to Points (Spatial Analyst)
#

import arcpy
from arcpy.sa import *
from arcpy import env 
for i in range(2018,2020):
    for j in range(1,13):
        if j < 10:
            filename = "c:/Users/DELL/Desktop/污水处理/北京2018-2019/" + str(i) + '0'+ str(j) + "rain-BJ.tif"
        elif j > 9:
            filename = "c:/Users/DELL/Desktop/污水处理/北京2018-2019/" + str(i) + str(j) + "rain-BJ.tif"
        env.workspace = filename
        shp = "c:/Users/DELL/Desktop/污水处理/Export_Output.shp"
        ExtractMultiValuesToPoints(shp, [[filename, filename[-17:-4]]], "NONE")


for i in range(2020,2023):
    for j in range(1,13):
        if j < 10:
            filename = "c:/Users/DELL/Desktop/污水处理/北京2020-2022/" + str(i) + '0'+ str(j) + "rain-BJ.tif"
        elif j > 9:
            filename = "c:/Users/DELL/Desktop/污水处理/北京2020-2022/" + str(i) + str(j) + "rain-BJ.tif"
        env.workspace = filename
        shp = "c:/Users/DELL/Desktop/污水处理/Export_Output.shp"
        ExtractMultiValuesToPoints(shp, [[filename, filename[-17:-4]]], "NONE")