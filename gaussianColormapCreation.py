#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 16:24:30 2023

@author: johnmallon

This program takes in a column of values from a '.csv' file and converts into into
RGB values. It uses the max of the absolute values to determine the RBG colormap.

Input: a '.csv' that has a column named 'gc' and that column has rows filled with
numbers

Output: a new '.csv' file saved to the same directory as the input file. It has the 
same name as the input file with the extension '_blenderColors.csv'

Red values are assigned to negative numbers and blue values to positive numbers. White
is assigned to values of zero.

User must change 'directory' and 'file' in the main function to be appropriate for
their input file (LINES 29 & 30)
"""

import pandas as pd
import matplotlib.colors as mcolors
import matplotlib.cm as cm

def main():
    directory = '/Users/johnmallon/Desktop/halofilin/Gaussian Curvatures/surface curvatures/Blender/Done/'
    file = 'blender_dHalAB_cell4_rod'
    df = pd.read_csv(directory+file+'.csv')
    df = df.dropna()
    values = df['gc'].values
    
    cmap = mcolors.LinearSegmentedColormap.from_list('custom_cmap', [(1,0,0),(1,1,1),(0,0,1)], N=32)
    colors = cm.ScalarMappable(cmap=cmap)
    vmin, vmax = values.min(), values.max()
    if abs(vmin)>vmax:
        vmax = vmin
    vmax = vmax*0.2
    colors.set_clim(vmin=-1*vmax,vmax=vmax)
    colormap = colors.to_rgba(values)
    
    red = []
    blue = []
    green = []
    for rgba in colormap:
        red.append(rgba[0])
        green.append(rgba[1])
        blue.append(rgba[2])      
     
    df['Red'] = red
    df['Green'] = green
    df['Blue'] = blue
    df.to_csv(directory+file+'_blenderColors.csv', index=False)
    
    
main()
