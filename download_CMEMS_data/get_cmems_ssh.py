#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 2022
@author: Jesus C. Compaire
@institution: Centro de Investigaciones del Mar y la Atmósfera (CIMA)
@position: Postdoctoral researcher
@e-mail:jesus.canocompaire@uca.es
"""
# %% Importing packages ####
import os
import motuclient
from cmems_motu import MotuOptions, motu_option_parser
import pwinput as pwi
# %% Data request using VIEW SCRIPT template from CMEMS
script_template = 'python -m motuclient\
    --motu https://my.cmems-du.eu/motu-web/Motu \
    --service-id SEALEVEL_GLO_PHY_L4_MY_008_047-TDS \
    --product-id cmems_obs-sl_glo_phy-ssh_my_allsat-l4-duacs-0.25deg_P1D \
    --longitude-min -60 --longitude-max -50 \
    --latitude-min -40 --latitude-max -33 \
    --date-min "2019-09-24 00:00:00" --date-max "2019-10-24 00:00:00" \
    --variable adt --variable crs --variable err_sla --variable err_ugosa \
    --variable err_vgosa --variable flag_ice --variable lat_bnds \
    --variable lon_bnds --variable nv --variable sla \
    --variable tpa_correction --variable ugos --variable ugosa \
    --variable vgos --variable vgosa \
    --variable lat_bnds --variable lon_bnds --variable nv \
    --variable sla \
    --out-dir <OUTPUT_DIRECTORY> --out-name <OUTPUT_FILENAME>\
    --user <USERNAME> --pwd <PASSWORD>'
# %% Define username, output directory and output name
query = input("Do you want to show the user's name?: [y/n]  ")
if query.lower() == 'y' or query.lower() == 'yes':
    USERNAME = input('Enter your CMEMS user name: ')
elif query.lower() == 'n'or query.lower() == 'no':
    USERNAME = pwi.pwinput(prompt = "Enter your CMEMS' user account name: ",
                        mask = '*') # Mask character
else:
    print("Please, answer the question: yes or no")
# Don't display anything when you enter the password
PASSWORD = pwi.pwinput('Enter your password: ',
                       mask ='')
# Path to save the download data in the current working directory.
# To use another directory, replace "os.getcwd()" with your desired path
OUTPUT_DIRECTORY = os.getcwd()
# Write a filename for the download data
OUTPUT_FILENAME = 'sea_surface_height_RdP.nc' 
# Set data request using motu
data_request = motu_option_parser(
    script_template, USERNAME, PASSWORD, OUTPUT_DIRECTORY, OUTPUT_FILENAME)
# Submit data request
motuclient.motu_api.execute_request(MotuOptions(data_request))
# To run the script press: Ctrl+F6 or Cmd+F6 (depending on your OS) and select
#       i)   "Run file with custom configuration",
#       ii)  "Execute in an external terminal".
#       iii) "Run".
# A terminal window will pop up asking you to write your CMEMS user's name
# and password. Then, the download process will start, and when is finished,
# the pops up window will close automatically.
#
