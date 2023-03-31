# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 22:17:48 2022

@author: DELL
"""
#%% code interpretation
# =============================================================================
# 1.To extract multi shp document according different land/vegetation cover
# 2.code in arcmap python command using arcmap'python (important,because arcpy doesn't work in anaconda)!!!!
# 3.code refer to the "help button" that commands right-click in acrmap (important too!!!)
# 4.two command merge (one is --spatial analyst tool--extraction--extract by attributes;
# the other is --conversion tools--from Raster--Raster To Polygon)
# =============================================================================
#%% DEMO one:extract grassland and transform it to shp document in China for further mask data

import arcpy
from arcpy import env
from arcpy.sa import *
import arcpy
from arcpy import env
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import scipy.io as scio
import scipy.stats as stats

for i in range(1982,2019):
    
    filename = r"I:\learn\GLASS_China_Land_Cover"+"\\"+ str(i)+"\\GLASS15B02.V40.A"+str(i)+"001.2020343.hdf"
    
    env.workspace = filename
    
    attExtract = ExtractByAttributes(filename, "VALUE = 3") # extract by attributes
    
    outExtractByMask = ExtractByMask(attExtract, "xinjiang.shp") # extract by mask
        
    arcpy.RasterToPolygon_conversion(outExtractByMask, r"C:\Users\DELL\Desktop\xibei_shp\\"+str(i)+".shp") # Raster To Polygon




#%% standard command in Arcmap
## 按属性提取(extract by attributes)
import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/sapyexamples/data"
attExtract = ExtractByAttributes("elevation", "VALUE > 1000") 
attExtract.save("c:/sapyexamples/output/attextract")

## 栅格转面(Raster To Polygon)
import arcpy
from arcpy import env
env.workspace = "C:/data"
arcpy.RasterToPolygon_conversion("zone", "c:/output/zones.shp", "NO_SIMPLIFY",
                                  "VALUE")


#%% mask data
import salem


#### NEE
ds = xr.open_dataset(r"E:\Research_life\DATA\xibei\NEE_mon_ANN.nc")

ds = ds.NEE


ds_mask_ANN = np.zeros((384,46,88))

for i in range(1982,2014):

    shp_path = r"C:\Users\DELL\Desktop\xibei_shp\\"+str(i)+".shp"

    ds_mask_ANN[12*(i-1982):12*(i-1981),::] = ds[12*(i-1982):12*(i-1981),::].salem.roi(shape=shp_path)



ds = xr.open_dataset(r"E:\Research_life\DATA\xibei\NEE_mon_MARS.nc")

ds = ds.NEE

ds_mask_MARS = np.zeros((384,46,88))

for i in range(1982,2014):

    shp_path = r"C:\Users\DELL\Desktop\xibei_shp\\"+str(i)+".shp"

    ds_mask_MARS[12*(i-1982):12*(i-1981),::] = ds[12*(i-1982):12*(i-1981),::].salem.roi(shape=shp_path)



ds = xr.open_dataset(r"E:\Research_life\DATA\xibei\NEE_mon_RF.nc")

ds = ds.NEE

ds_mask_RF = np.zeros((384,46,88))

for i in range(1982,2014):

    shp_path = r"C:\Users\DELL\Desktop\xibei_shp\\"+str(i)+".shp"

    ds_mask_RF[12*(i-1982):12*(i-1981),::] = ds[12*(i-1982):12*(i-1981),::].salem.roi(shape=shp_path)


#### GPP

ds = xr.open_dataset(r"E:\Research_life\DATA\xibei\GPP_mon_ANN.nc")

ds = ds.GPP

ds_mask_ANN = np.zeros((384,46,88))

for i in range(1982,2014):

    shp_path = r"C:\Users\DELL\Desktop\xibei_shp\\"+str(i)+".shp"

    ds_mask_ANN[12*(i-1982):12*(i-1981),::] = ds[12*(i-1982):12*(i-1981),::].salem.roi(shape=shp_path)



ds = xr.open_dataset(r"E:\Research_life\DATA\xibei\GPP_mon_MARS.nc")

ds = ds.GPP

ds_mask_MARS = np.zeros((384,46,88))

for i in range(1982,2014):

    shp_path = r"C:\Users\DELL\Desktop\xibei_shp\\"+str(i)+".shp"

    ds_mask_MARS[12*(i-1982):12*(i-1981),::] = ds[12*(i-1982):12*(i-1981),::].salem.roi(shape=shp_path)



ds = xr.open_dataset(r"E:\Research_life\DATA\xibei\GPP_mon_RF.nc")

ds = ds.GPP

ds_mask_RF = np.zeros((384,46,88))

for i in range(1982,2014):

    shp_path = r"C:\Users\DELL\Desktop\xibei_shp\\"+str(i)+".shp"

    ds_mask_RF[12*(i-1982):12*(i-1981),::] = ds[12*(i-1982):12*(i-1981),::].salem.roi(shape=shp_path)





## due to 
scio.savemat(r"E:\Research_life\DATA\xibei\NEE_mon_ds_mask__ANN.mat",{'ds_mask_ANN':ds_mask_ANN})
scio.savemat(r"E:\Research_life\DATA\xibei\NEE_mon_ds_mask__MARS.mat",{'ds_mask_MARS':ds_mask_MARS})
scio.savemat(r"E:\Research_life\DATA\xibei\NEE_mon_ds_mask__RF.mat",{'ds_mask_RF':ds_mask_RF})

scio.savemat(r"E:\Research_life\DATA\xibei\GPP_mon_ds_mask__ANN.mat",{'ds_mask_ANN':ds_mask_ANN})
scio.savemat(r"E:\Research_life\DATA\xibei\GPP_mon_ds_mask__MARS.mat",{'ds_mask_MARS':ds_mask_MARS})
scio.savemat(r"E:\Research_life\DATA\xibei\GPP_mon_ds_mask__RF.mat",{'ds_mask_RF':ds_mask_RF})


## filter monthly VALUE < 0
ds_mask_ANN[ds_mask_ANN < 0] = np.nan
ds_mask_MARS[ds_mask_MARS < 0] = np.nan
ds_mask_RF[ds_mask_RF < 0] = np.nan

## filter multi year VALUE < 0
dataset = np.nanmean(ds_mask.values,0)
dataset[dataset<0] = np.nan
mask_loc = np.isnan(dataset)
da = np.zeros((384,46,88)) #384 month
for i in range(384): #384 month
    ans = np.ma.masked_array((ds_mask.values[i,::]),mask=[mask_loc])
    da[i,::] = ans.filled(fill_value=np.nan)



## filter monthly VALUE < 0
ds_mask_ANN[ds_mask_ANN < 0] = np.nan
ds_mask_MARS[ds_mask_MARS < 0] = np.nan
ds_mask_RF[ds_mask_RF < 0] = np.nan


## filter multi year VALUE < 0
def filter_multi_year(ds_mask):
    dataset = np.nanmean(ds_mask,0)
    dataset[dataset<0] = np.nan
    mask_loc = np.isnan(dataset)
    da = np.zeros((384,46,88)) #384 month
    for i in range(384): #384 month
        ans = np.ma.masked_array((ds_mask[i,::]),mask=[mask_loc])
        da[i,::] = ans.filled(fill_value=np.nan)
    return da


## month to year
data = ds_mask_ANN
# data = ds_mask_MARS
# data = ds_mask_RF

nee = np.zeros((32,46,88))

for i in range(32):
    
    nee[i,::] = np.nansum(data[12*i:12*(i+1),::],0)

IAV = np.nanmean(nee,(1,2))

#### slope computing ####
turn_point1 = 8
turn_point2 = 19
turn_point3 = 32

x = np.arange(1982,2014,1)

x1 = x[:turn_point1]
y_ndvi = IAV[:turn_point1]

slope1, c1, r_value, p1_value, std_err = stats.linregress(x1, y_ndvi)
# print(p1_value)
# print(slope1)

x2 = x[turn_point1:turn_point2]
y_ndvi = IAV[turn_point1:turn_point2]
slope2, c2, r_value, p2_value, std_err = stats.linregress(x2, y_ndvi)
# print(p2_value)
# print(slope2)

x3 = x[turn_point2:turn_point3]
y_ndvi = IAV[turn_point2:turn_point3]
slope3, c3, r_value, p3_value, std_err = stats.linregress(x3, y_ndvi)
# print(p3_value)
# print(slope3)


#### graph
from matplotlib import rcParams

config = {
        "font.family": 'Times new roman',
        "font.size"  : 18,
        "font.serif" : ['SimSun'],
        "mathtext.fontset" : 'stix',
        "axes.unicode_minus": False
            
            }

rcParams.update(config)

plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'


x = np.arange(1982,2014,1)

y = IAV

fig = plt.figure(figsize=(20,10), dpi=200)

ax = fig.add_subplot(111)

# ax.plot(x, y, marker='o', alpha = 0.7, markersize=20, markerfacecolor= 'g', linewidth=3, color='g', linestyle='-', label='$\mathrm{Interannual}$ $\mathrm{variation}$ $\mathrm{of}$ $\mathrm{NEE}$')
ax.plot(x, y, marker='o', alpha = 0.7, markersize=20, markerfacecolor= 'g', linewidth=3, color='g', linestyle='-', label='$\mathrm{Interannual}$ $\mathrm{variation}$ $\mathrm{of}$ $\mathrm{GPP}$')


ax.plot(x1, slope1 * x1 + c1, alpha = 0.8, color='k', linestyle='--', linewidth = 4)
ax.plot(x2, slope2 * x2 + c2, alpha = 0.8, color='k', linestyle='--', linewidth = 4)
ax.plot(x3, slope3 * x3 + c3, alpha = 0.8, color='k', linestyle='--', linewidth = 4)

# plt.grid(alpha=0.6)

plt.xticks(range(1982,2014,5),fontsize = 24)
plt.yticks(fontsize = 24)


plt.xlabel('$\mathrm{Year}$',fontsize = 32, labelpad=15)

# plt.ylabel('$\mathrm{NEE(gC/m^2/year)}$',fontsize = 32, labelpad=15)
plt.ylabel('$\mathrm{GPP(gC/m^2/year)}$',fontsize = 32, labelpad=15)

plt.legend(fontsize=24, loc=4, bbox_to_anchor=(0.95,0.09),ncol=1,fancybox=True,shadow=False,frameon=False)

plt.axvline(1989,c='k',ls='-.',lw=3)

plt.axvline(2002,c='k',ls='-.',lw=3)

# plt.fill_between(np.arange(1980,1990), 73,83,facecolor='lightyellow', alpha=0.4)
# plt.fill_between(np.arange(1989,2003), 73,83,facecolor='lightgray', alpha=0.4)
# plt.fill_between(np.arange(2002,2021), 73,83,facecolor='wheat', alpha=0.4)


plt.xlim(1981,2014)
# plt.ylim(73,83)