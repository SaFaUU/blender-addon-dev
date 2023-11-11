bl_info = {
    "name": "Simple Button",
    "author": "Safa",
    "version": (1, 0),
    "blender": (3, 6, 5),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Simple Button",
    "warning": "",
    "doc_url": "",
    "category": "",
}

import bpy

class ButtonOperator1(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.1"
    bl_label = ""
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        bpy.ops.transform.translate(value=(0, 0, 1), orient_type='LOCAL')
        return {'FINISHED'}
    
class ButtonOperator2(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.2"
    bl_label = ""
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        bpy.ops.transform.translate(value=(0, 0, -1), orient_type='LOCAL')
        return {'FINISHED'}
    
class ButtonOperator3(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.3"
    bl_label = ""
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        bpy.ops.transform.resize(value=(2, 2, 2), orient_type='GLOBAL')

        return {'FINISHED'}
    
class ButtonOperator4(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.4"
    bl_label = ""
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        bpy.ops.transform.resize(value=(-0.5, -0.5, -0.5), orient_type='GLOBAL')

        return {'FINISHED'}
    
class CustomPanel(bpy.types.Panel):
    bl_label = ""
    bl_idname = "OBJECT_PT_custom1"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        
        row.operator(ButtonOperator1.bl_idname, text=ButtonOperator1.bl_label, icon="TRIA_UP")
        row.operator(ButtonOperator2.bl_idname, text=ButtonOperator2.bl_label, icon="TRIA_DOWN")
        row.operator(ButtonOperator3.bl_idname, text=ButtonOperator3.bl_label, icon="ADD")
        row.operator(ButtonOperator4.bl_idname, text=ButtonOperator4.bl_label, icon="REMOVE")
        
from bpy.utils import register_class, unregister_class

_classes = [
    ButtonOperator1,
    ButtonOperator2,
    ButtonOperator3,
    ButtonOperator4,
    CustomPanel
]

def register():
    for cls in _classes:
        register_class(cls)

def unregister():
    for cls in _classes:
        unregister_class(cls)
        
if __name__ == "__main__":
    register()