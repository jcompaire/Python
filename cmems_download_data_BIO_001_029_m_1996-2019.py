#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 31 14:49:17 2021
@author: Jesus C. Compaire
@institution: Centro de Investigaciones del Mar y la Atmósfera (CIMA)
@position: Postdoctoral researcher
@e-mail:jesus.canocompaire@cima.fcen.uba.ar
"""
# %% import getpass
import sys
sys.path.append("/home/gsus/.local/lib/python3.5/site-packages/")
import motuclient
from cmems_motu import MotuOptions, motu_option_parser
# Data request using VIEW SCRiPT template in CMEMS
#--date-min "1996-01-16 12:00:00" --date-max "2019-11-15 23:56:15"\
script_template = 'python -m motuclient\
    --motu https://my.cmems-du.eu/motu-web/Motu \
    --service-id GLOBAL_REANALYSIS_BIO_001_029-TDS \
    --product-id global-reanalysis-bio-001-029-monthly \
    --longitude-min -60 --longitude-max -50 \
    --latitude-min -40 --latitude-max -33 \
    --date-min "1993-01-01 12:00:00" --date-max "1995-12-31 12:00:00"\
    --depth-min 0.5056 --depth-max 0.5059 \
    --variable chl --variable nppv \
    --out-dir <OUTPUT_DIRECTORY> --out-name <OUTPUT_FILENAME>\
    --user <USERNAME> --pwd <PASSWORD>'
# Define username, output directory and output name
USERNAME = 'jcanocompaire'
import os; OUTPUT_DIRECTORY = os.getcwd()
# OUTPUT_FILENAME = 'BIO_001_029_monthly_1996to2019.nc'
OUTPUT_FILENAME = 'BIO_001_029_monthly_1993to1995.nc'
# Set data request
import maskpass
data_request = motu_option_parser(
    script_template, USERNAME,
    maskpass.advpass(), OUTPUT_FILENAME)
# Submit data request
motuclient.motu_api.execute_request(MotuOptions(data_request))




















