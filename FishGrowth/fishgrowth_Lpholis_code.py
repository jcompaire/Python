#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 2024
@author: Jesus C. Compaire
@institution: Centro para el Estudio de Sistemas Marinos (CESIMAR)
@position: Postdoctoral researcher
@e-mail:jesus.canocompaire@uca.es
"""
# %% Script description
## -- -- -- -- -- -- -- -- -- -- -- -- --
##
## With this script you will be able to repliacte the Figures 2 and 3 of the
## manuscript Compaire et al. (2024).
## To learn more about this study, you may read the manuscript Compaire et al. 
## (2024). Whilst for a detailed the description of each variable included in
## the dataset check Compaire et al. (2021).
##
## References:
##
## Compaire, J. C, Visintini, N., Soriguer, M. C., Johnson, M. L., Hull, S. &
## Barrett, C. J. (2024). Lipophrys pholis is larger, grows faster and is in
## better condition in protected than in unprotected rocky shores.
## Aquatic Conservation: Marine and Freshwater Ecosystems, 34(2), e4083.
## https://doi.org/10.1002/aqc.4083
##
## Compaire, J. C, Visintini, N., Soriguer, M. C., Johnson, M. L., Hull, S. &
## Barrett, C. J. (2021). Length and weight data of common blenny
## Lipophrys pholis (Blenniidae) caught from tide pools in two contrasting 
## marine provinces in the temperate Northern Atlantic. PANGAEA,
## https://doi.pangaea.de/10.1594/PANGAEA.932955
##
## -- -- -- -- -- -- -- -- -- -- -- -- --
#
# %% Importing packages ####
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from pangaeapy import PanDataSet
# %% Accesing data hosted in PANGAEA digital repository
ds = PanDataSet('10.1594/PANGAEA.932955')
# print(ds.title, ds.abstract, ds.citation)
df = pd.DataFrame(ds.data.values, columns= ds.data.columns)
dataset = df.iloc[:,[1, 2, 11, 12]] # subsetting dataframe
dataset.set_axis(["Shore", "Province", "TL_cm", "WT_g"],
                 axis = 1, inplace = True) # renaming columns
# The latest version of pandas does not have the argument inplace, so run 
# dataset = dataset.set_axis(
    # axis = 1,
    # labels = ["Shore", "Province", "TL_cm", "WT_g"]) # renaming columns
# ============================================================================
# %% Length distribution for each population (Figure 2)
# Nested loops to iterate over the combination of 'Shore' & 'Province' values,
# sets the label dinamically, and determines the color based on the conditions
shore_values = ["Protected", "Unprotected"]
province_values = ["Lusitania", "Northern European Seas"]
# Density plot
cp = sns.color_palette("husl", 6) # color palette
plt.figure(figsize=(200,200), dpi= 300)
fig, ax = plt.subplots()
for shore in shore_values:
    for province in province_values:
        label = f"{shore} {province}"
        color_index = 5 if shore == "Protected" else 0
        if province == "Northern European Seas":
            color_index = 2 if shore == "Protected" else 4
        sns.kdeplot(dataset.loc[
            (dataset['Shore'] == shore) & (dataset['Province'] == province),
            "TL_cm"],
            shade = False, color = cp[color_index], label = label,
            alpha = 1, linestyle = '-', linewidth = 1,
            marker = "", markersize = 1)
        font = FontProperties()
        font.set_style('normal') # italic
        fontparams = {'font.size': 9, 'font.weight':'bold', # bold
                      'font.family':'Times New Roman', # serif
                      'font.style':'normal'} # italic
        plt.rcParams.update(fontparams)
plt.legend(["Protected LU",
            "Protected NES",
            "Unprotected LU",
            "Unprotected NES"],
           labelspacing = 2, frameon = False )
plt.xlabel('Total length (cm)', fontproperties=font)
plt.ylabel('Density', fontproperties=font)
# plt.show()
plt.savefig("Fig2_density.eps", format='eps')
plt.close()
# %% Length-weight relationships (LWR) for each population (Figure 3)
lv = np.arange(0, 16.1, 0.1) # vector
# "a" & "b" parameters of the LWR come from Compaire et al. (2024)
lines = pd.DataFrame(
    {'Protected LU': (0.0080*lv**3.173),
    'Protected NES': (0.0101*lv**3.110),
    'Unprotected LU': (0.0079*lv**3.125),
    'Unprotected NES': (0.0109*lv**2.949)}
    )
cl = [5, 2, 0, 4] # selecting color for lines
sdot = 20 # markers size
mk = ["o", "s", "o","^"] # markers type
order_ln = [2,4,3,1] # order lines
order_mk = [8,7,5,6] # order markers
plt.figure(figsize=(200,200), dpi= 300)
fig, ax = plt.subplots()
column_names = lines.columns
for i, column_names in enumerate(column_names, start = 0):
    plt.plot(lv, lines[column_names], '-',
             c = cp[cl[i]], zorder = order_ln[i])
plt.legend(["Protected LU",
            "Protected NES",
            "Unprotected LU",
            "Unprotected NES"],
           prop = {'weight':'bold'},
           labelspacing = 2, frameon = False )
for shore in shore_values:
        for province in province_values:
            label = f"{shore} {province}"
            color_index = 5 if shore == "Protected" else 0
            marker_index = 0 if shore == "Protected" else 0
            zo = 7 if shore == "Protected" else 5
            if province == "Northern European Seas":
                color_index = 2 if shore == "Protected" else 4
                marker_index = 1 if shore == "Protected" else 3
                zo = 8 if shore == "Protected" else 6
            scatter_data = dataset.loc[
                (dataset['Shore'] == shore) &
                (dataset['Province'] == province),
                ["TL_cm", "WT_g"]
                ]
            plt.scatter(scatter_data["TL_cm"], scatter_data["WT_g"],
                        alpha = 1, marker = mk[marker_index],
                        c = cp[color_index],
                        s = sdot, edgecolor ='black',
                        linewidth = 0.5, zorder = zo, label = label)
        font = FontProperties()
        font.set_style('normal') # italic
        fontparams = {'font.size': 9, 'font.weight':'bold', # normal
                      'font.family':'Times New Roman', # serif
                      'font.style':'normal'} # italic
        plt.rcParams.update(fontparams)
        plt.rcParams['mathtext.default'] = 'regular'
        plt.xlabel('Total length (cm)', fontproperties=font)
        plt.ylabel('Total weight (g)', fontproperties=font)
        # 
        x=5.5
        ax.text(x, 54.5, r'$WT=0.0080*TL^{3.173}$', fontsize=8, color='k')
        ax.text(x, 47.3, r'$WT=0.0101*TL^{3.110}$', fontsize=8, color='k')
        ax.text(x, 40, r'$WT=0.0079*TL^{3.125}$', fontsize=8, color='k')
        ax.text(x, 32.3, r'$WT=0.0109*TL^{2.949}$', fontsize=8, color='k')
# plt.show()
# #  Save
plt.savefig("Fig3_LWRs_.eps",format='eps')   
plt.close()
