# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 21:48:31 2022

@author: DELL
"""
#%% code interpretation
# =============================================================================
# count amount of pixel to further compute percentage of cultivated land
# 
# 
# 
# 
# =============================================================================
#%%
import arcpy
from arcpy import env
from arcpy.sa import *

for j in range(1,16):

    for i in range(1982,2019):   
             
        filename = r"D:\China_Land_Cover"+"\\"+ str(i)+"\\GLASS15B02.V40.A"+str(i)+"001.2020343.hdf"
        
        env.workspace = filename
                
        shp_name = "C:/Users/DELL/Desktop/xijiang/shp/" + str(j) + "/Export_Output.shp"
        
        outExtractByMask = ExtractByMask(filename, shp_name) # extract by mask
                                
        GPP_outputfile = "C:/Users/DELL/Desktop/xibei/" + str(j) + "/" + str(i) + ".nc"
        
        arcpy.RasterToNetCDF_md(outExtractByMask, GPP_outputfile)
        
       