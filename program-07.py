#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 13:33:32 2020

@author: jtellier
"""

""" Created by Joshua Tellier on 2/28/2020, Purdue University. The purpose of
this file is to produce various graphics for the analysis of USGS earthquake data. The code will run properly
if a csv file named 'all_month.csv' is present in the current working directory and said file contains
the correct variables as included in the USGS earthquake tracking database."""

"""User note: If NOT using inline graphics, must close out of graphics window between plots to avoid plots overlaying each other """

import pandas
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import pylab

data = pandas.read_table('all_month.csv', sep=',')
""" Now we must remove any observations for which one or more columns contain an "NaN" value because retaining NaN's prevents matplotlib from successfully graphing the data """
refined_data = data.dropna(axis=0, subset=['mag']) #this line removes any rows for which the magnitude column has a value of NaN
print(data.shape) #now we check to see how many rows were removed by looking at the shapes of the respective data frames
print(refined_data.shape)
plt.hist(refined_data['mag'], bins=10, range=(0,10)) #the histogram
plt.xlabel('Magnitude', fontsize=10)
plt.ylabel('Frequency', fontsize=10)

sns.kdeplot(np.array(refined_data['mag']),kernel='gau',bw=0.2) #The KDE plot; gaussian kernel type, kernel width of 0.2
plt.xlabel('Magnitude', fontsize=10)
plt.ylabel('Density', fontsize=10)
#Histogram and kdeplot both show a major peak around 1-2 magnitude, and a second smaller peak at just above 4 magnitude. Overall shape is similar.
#Histogram loses a lot more info than the kde plot due to bin size, but the kde plot may be more misleading because it shows the erroneous possibility for negative magnitude.

plt.scatter(refined_data['longitude'],refined_data['latitude'],c='r',marker='+') #the scatter plot for lat-long data
plt.xlabel('Longitude', fontsize=10) #axes labels
plt.ylabel('Latitude', fontsize=10)

fig,ax = plt.subplots()
ax.plot(np.sort(refined_data['depth']),np.linspace(0.0,1.0,len(refined_data['depth']))) #normalized cumulative distribution plot of earthquake depth
plt.xlabel('Depth (km)', fontsize=10) #axes labels
plt.ylabel('Cumulative Proportion of All Sites', fontsize=10)

plt.scatter(refined_data['mag'],refined_data['depth'],c='g',marker='.') #scatter plot of magnitude (x-axis) with depth (y-axis)
plt.xlabel('Magnitude', fontsize=10) #axes labels
plt.ylabel('Depth (km)', fontsize=10)

stats.probplot(refined_data['mag'], dist='norm',plot=pylab) #Q-Q plot of earthquake magnitudes assuming normal distribution
