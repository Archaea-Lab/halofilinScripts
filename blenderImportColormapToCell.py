"""
Created on Fri Dec  8 16:24:30 2023

@author: johnmallon

This program takes the output file from 'gaussianColormapCreation.py' and colors the
surface of a '.ply' cell file in the software Blender

This program was executed in Blender using the text editor window by copy and pasting
it there. The files we are inputing has the red, green, and blue values in the
18th, 19th, and 20th columns (index zero) respectively. If for whatever reason your 
RGB values are in different columns you have to change the script accordingly at
commented area (LINES 43-45).

You must change the directory ('data') on LINE 24 accordingly to point to your RGB data that was output
from 'gaussianColormapCreation.py'

Following running this in Blender you must create a material containing the color
before rendering an image.
"""

import bpy, csv

data = '/Users/johnmallon/Desktop/halofilin/Gaussian Curvatures/surface curvatures/Blender/Done/blender_dHalAB_cell4_rod_blenderColors.csv'
colordata = []
with open(data) as csvfile:
    rdr =csv.reader( csvfile )
    for row in rdr:
        colordata.append(row)
bpy.ops.object.mode_set(mode = 'OBJECT')
obj = bpy.context.active_object
bpy.ops.paint.vertex_paint_toggle()
bpy.context.object.data.use_paint_mask_vertex = True
for i in range(len(colordata)-1):
    bpy.ops.object.mode_set(mode = 'EDIT') 
    bpy.ops.mesh.select_mode(type="VERT")
    bpy.ops.mesh.select_all(action = 'DESELECT')
    bpy.ops.object.mode_set(mode = 'OBJECT')
    obj.data.vertices[i].select = True
    bpy.ops.paint.vertex_paint_toggle()
    
    #change values here to your respective columns if need be
    red = float(colordata[i+1][18])
    green = float(colordata[i+1][19])
    blue = float(colordata[i+1][20])
    
    bpy.data.brushes["Draw"].color = (red,green,blue)
    bpy.ops.paint.vertex_color_set()
    bpy.ops.object.mode_set(mode = 'OBJECT')
    bpy.ops.paint.vertex_paint_toggle()
