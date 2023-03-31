# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 18:17:28 2022

@author: DELL
"""
#%% code interpretation
# =============================================================================
# fifteen cities shp transform to netcdf document
# 
# 
# 
# 
# 
# =============================================================================
#%%
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import scipy.io as scio
import scipy.stats as stats

import arcpy
from arcpy import env
from arcpy.sa import *
import arcpy
from arcpy import env
#%% GPP ANN

for j in range(1,16):
    
    for i in range(1982,2014):
        
        filename = r"I:\learn\GLASS_China_Land_Cover"+"\\"+ str(i)+"\\GLASS15B02.V40.A"+str(i)+"001.2020343.hdf"
        
        env.workspace = filename
        
        attExtract = ExtractByAttributes(filename, "VALUE = 3") # extract by attributes

        shp_name = "C:/Users/DELL/Desktop/xijiang/shp/" + str(j) + "/Export_Output.shp"
        
        outExtractByMask = ExtractByMask(attExtract, shp_name) # extract by mask   
        
        GPP_inputfile = r"E:\Research_life\DATA\FLUXCOM\raw\annual\annual\annual\GPP.ANN.CRUNCEPv6.annual."+str(i)+".nc"
        
        GPP = arcpy.MakeNetCDFRasterLayer_md(GPP_inputfile)
                
        outExtractByMask1 = ExtractByMask(GPP, shp_name) # extract by mask   
        
        GPP_outputfile = "C:/Users/DELL/Desktop/xinjiang_GPP/GPP_ANN/" + str(j) + "/" + str(i) + ".nc"
                
        arcpy.RasterToNetCDF_md(outExtractByMask1, GPP_outputfile)

#%% GPP MARS

for j in range(1,16):
    
    for i in range(1982,2014):
        
        filename = r"I:\learn\GLASS_China_Land_Cover"+"\\"+ str(i)+"\\GLASS15B02.V40.A"+str(i)+"001.2020343.hdf"
        
        env.workspace = filename
        
        attExtract = ExtractByAttributes(filename, "VALUE = 3") # extract by attributes

        shp_name = "C:/Users/DELL/Desktop/xijiang/shp/" + str(j) + "/Export_Output.shp"
        
        outExtractByMask = ExtractByMask(attExtract, shp_name) # extract by mask   
        
        GPP_inputfile = r"E:\Research_life\DATA\FLUXCOM\raw\annual\annual\annual\GPP.MARS.CRUNCEPv6.annual."+str(i)+".nc"
        
        GPP = arcpy.MakeNetCDFRasterLayer_md(GPP_inputfile)
                
        outExtractByMask1 = ExtractByMask(GPP, shp_name) # extract by mask   
        
        GPP_outputfile = "C:/Users/DELL/Desktop/xinjiang_GPP/GPP_MARS/" + str(j) + "/" + str(i) + ".nc"
                
        arcpy.RasterToNetCDF_md(outExtractByMask1, GPP_outputfile)
        
#%% GPP RF


for j in range(1,16):
    
    for i in range(1982,2014):
        
        filename = r"I:\learn\GLASS_China_Land_Cover"+"\\"+ str(i)+"\\GLASS15B02.V40.A"+str(i)+"001.2020343.hdf"
        
        env.workspace = filename
        
        attExtract = ExtractByAttributes(filename, "VALUE = 3") # extract by attributes

        shp_name = "C:/Users/DELL/Desktop/xijiang/shp/" + str(j) + "/Export_Output.shp"
        
        outExtractByMask = ExtractByMask(attExtract, shp_name) # extract by mask   
        
        GPP_inputfile = r"E:\Research_life\DATA\FLUXCOM\raw\annual\annual\annual\GPP.RF.CRUNCEPv6.annual."+str(i)+".nc"
        
        GPP = arcpy.MakeNetCDFRasterLayer_md(GPP_inputfile)
                
        outExtractByMask1 = ExtractByMask(GPP, shp_name) # extract by mask   
        
        GPP_outputfile = "C:/Users/DELL/Desktop/xinjiang_GPP/GPP_RF/" + str(j) + "/" + str(i) + ".nc"
                
        arcpy.RasterToNetCDF_md(outExtractByMask1, GPP_outputfile)