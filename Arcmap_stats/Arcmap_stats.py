# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 01:21:15 2022

@author: DELL
"""
#%% code interpretation
# =============================================================================
# 1.combined with Arcmap_extract_by_land_cover_for_xibei_everycity.py and Arcmap_extract_by_landcover_for_count.py
# 2.statistic work
# =============================================================================

#%%
import xarray as xr
import numpy as np
import scipy.io as scio
import pandas as pd 

GPP_ANN = np.zeros((15,32))

for i in range(1,16):
    
    for j in range(1982,2014):
        
        ds = xr.open_dataarray(r"C:\Users\DELL\Desktop\xinjiang_GPP\GPP_ANN\\"+str(i)+"\\"+str(j)+".nc")
    
        GPP_ANN[i-1,j-1982] = ds.mean().values




GPP_MARS = np.zeros((15,32))

for i in range(1,16):
    
    for j in range(1982,2014):
        
        ds = xr.open_dataarray(r"C:\Users\DELL\Desktop\xinjiang_GPP\GPP_MARS\\"+str(i)+"\\"+str(j)+".nc")
    
        GPP_MARS[i-1,j-1982] = ds.mean().values




GPP_RF = np.zeros((15,32))

for i in range(1,16):
    
    for j in range(1982,2014):
        
        ds = xr.open_dataarray(r"C:\Users\DELL\Desktop\xinjiang_GPP\GPP_RF\\"+str(i)+"\\"+str(j)+".nc")
    
        GPP_RF[i-1,j-1982] = ds.mean().values


pd.DataFrame(GPP).to_excel(r"C:\Users\DELL\Desktop\xinjiang_GPP\xinjiang_GPP_ANN.xlsx")

pd.DataFrame(GPP).to_excel(r"C:\Users\DELL\Desktop\xinjiang_GPP\xinjiang_GPP_MARS.xlsx")

pd.DataFrame(GPP).to_excel(r"C:\Users\DELL\Desktop\xinjiang_GPP\xinjiang_GPP_RF.xlsx")


#%%

rate = np.zeros((15,10,37))

for i in range(1,16):

    for j in range(1982,2019):
    
        ds = xr.open_dataarray(r"C:\Users\DELL\Desktop\rate\\"+str(i)+"\\"+str(j)+".nc")
        
        data = ds.values    
        
        for k in range(10):
            
            rate[i-1,k,j-1982] = np.sum(data==k)


scio.savemat(r"C:\Users\DELL\Desktop\rate\rate.mat", {'rate':rate})
