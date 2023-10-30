import csv
import bpy

with open("F:/Programming Tutorials/Python Project/blender-addon-dev/test.csv", "r") as f:
    readout = list(csv.reader(f))
    bpy.ops.object.text_add()
    obj = bpy.context.object
    obj.data.body =  str(readout)
    
    print(readout)