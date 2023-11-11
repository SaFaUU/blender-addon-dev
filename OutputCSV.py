import bpy

outputFile = "F:/Programming Tutorials/Python Project/blender-addon-dev/empty.csv"

csvLines = ["[Hello, Safa, 1, 2 ,3]"]

f = open(outputFile, "w")
f.writelines(csvLines)
f.close()