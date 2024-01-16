#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 11:07:55 2023

@author: johnmallon

This program takes intensity values or grey values from a 3D stack of images and pairs
them with gaussian curvature values measured at a cells surface.

INPUT: A '.csv' file containing gaussian curvature data generated from LimeSeg and
a '.tif' file containing a 3D stack of images

OUTPUT: A '.csv' file containing cell surface gaussian curvature data paired with their
corresponding, background subtracted, grey value/intensity.

You must change the directory accordingly to point to where the two input files reside.
You must change the file name accordingly to the file containing the curvature data.
Your 3D stack '.tif' files must have the prefix 'C2-' to work correctly.
"""


import pandas as pd
from skimage import io

def main():
    directory = '/Users/johnmallon/Desktop/halofilin/Gaussian Curvatures/HalA_GFP (aJK03)/'
    file = 'ajk03_summary.csv'
    df = pd.read_csv(directory+file)
    df = df.loc[df['morphology']=='disks']
    gcs = df['gc'].to_list()
    
    df['pos_x']=round(df['pos_x'],0)
    df['pos_y']=round(df['pos_y'],0)
    #Z axis must be converted from LimeSeg parameters
    df['pos_z']=round((df['pos_z']/4.307),0)
    
    intensities = []
    for index, value in df.iterrows():
        imageName = value['file_name']
        imageName = 'C2-'+imageName[:-4]+'.tif'
        im = io.imread(directory+imageName)
        background = 106
        x = int(value['pos_x'])
        y = int(value['pos_y'])
        z = int(value['pos_z'])
        #skimage stores 3d images as z,y,x not x,y,z
        intensities.append((im[z][y][x])-background)
    
    outDF = pd.DataFrame()
    outDF['Gaussian Curvature'] = gcs
    outDF['Grey Value (Background Subtracted)'] = intensities
    outDF.to_csv(directory+"filamentLocations_halA_disks.csv", index=False)   
    
main()