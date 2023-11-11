import bpy

outputFile = "F:/Programming Tutorials/Python Project/blender-addon-dev/empty.txt"

txtLines = ["Hello Safa"]

f = open(outputFile, "w")
f.writelines(txtLines)
f.close()