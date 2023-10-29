import bpy
from bpy import data as D
from bpy import context as C
from mathutils import *
from math import *
from random import randint



for i in range(20):
    x =randint(-10, 10)
    y =randint(-10, 10)
    z =randint(-10, 10)
    bpy.ops.mesh.primitive_cube_add(size=2, calc_uvs=True, enter_editmode=False, align='WORLD', location=(x, y, z), scale=(1, 1, 1))

