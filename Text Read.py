import csv
import bpy

with open("F:/Programming Tutorials/Python Project/blender-addon-dev/normal.txt", "r") as f:
    readout = f.read()
    bpy.ops.object.text_add()
    obj = bpy.context.object
    obj.data.body =  str(readout)
    
    print(readout)