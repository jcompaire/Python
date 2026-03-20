#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 2022
@author: Jesus C. Compaire
@institution: Centro de Investigaciones del Mar y la Atmósfera (CIMA)
@position: Postdoctoral researcher
@e-mail:jesus.canocompaire@cima.fcen.uba.ar
"""
import matplotlib.pyplot as plt
# Load package to interact with NetCDF file
import xarray as xr
# Open and Read the file
DS_sst = xr.open_dataset('sea_surface_temperature_RdP.nc')
DS_ssh = xr.open_dataset('sea_surface_height_RdP.nc')
DS_chl = xr.open_dataset('chlorophyll_a_in_sea_water_RdP.nc')

print(DS_sst)
print(DS_ssh)
print(DS_chl)
# DS.analysed_sst.sel(time='2019-10-06').plot()
#
sst = DS_sst.analysed_sst.sel(time='2019-10-06')
ssh = DS_ssh.adt.sel(time='2019-10-06')
chl = DS_chl.chl.sel(time='2019-10-06')

# Prepare the figure
f, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(14, 4))
# Plot data
sst.plot(ax=ax1, cmap=plt.cm.rainbow)
ax1.set_title('')
# sst.set_title('Celsius: default')
# sst.set_xlabel('')
# sst.set_ylabel('')
ssh.plot(ax=ax2, cmap=plt.cm.coolwarm)
ax2.set_title('')
chl.plot(ax=ax3, cmap=plt.cm.viridis)
ax3.set_title('')
# Show plots
plt.tight_layout()
plt.show()
