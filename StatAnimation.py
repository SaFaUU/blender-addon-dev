import bpy
import csv 
from math import *

bar_spacing = 1
bar_width = 2

with open("F:/Programming Tutorials/Python Project/blender-addon-dev/GDP.csv") as f:
    readout = list(csv.reader(f))
    
line_length = len(readout[1])-1

for i in readout:
    placement = readout.index(i)
    bpy.ops.mesh.primitive_plane_add(size=1)
    bar = bpy.context.object
    for vert in bar.data.vertices:
        vert.co[1] +=0.5
        vert.co[0] += placement * bar_spacing + 0.5
    frame_number = 1
    a = 1
    
    for b in range(line_length):
        bpy.context.scene.frame_set(frame_number)
        bar.scale = (1, float(i[a])/4, 1)
        bar.keyframe_insert(data_path = "scale", index = 1)
        frame_number += 20
        a+=1
        
    bpy.ops.object.text_add()
    text= bpy.context.object
    text.data.align_x = "RIGHT"
    text.data.align_y = "CENTER"
    text.rotation_euler= (0, 0, 1.5708)
    bpy.ops.transform.translate(value = (placement * bar_spacing + 0.5, -0.5, 0))
    text.data.body = str(i[0])
    
    solid_mod = bar.modifiers.new("solidy", "SOLIDIFY")
    solid_mod.thickness = 0.3
    solid_mod2 = text.modifiers.new("solidy", "SOLIDIFY")
    solid_mod2.thickness = 0.3
    