import bpy
from bpy.props import PointerProperty

from .properties import *
from .panels import *
from .operators import *

# =====================================================
#                      Registration
# =====================================================

classes = [
    OMT_Properties,
    OMT_Measures,
    OMT_Assign_Edge_Banding,
    OMT_Material_Edge_Banding,
    OMT_Colors_Edge_Banding,
    OMT_Place_Objects,
    OMT_Standards,
    OMT_Legacy_Panel,
    OMT_Create_Materials_from_Excel,
    OMT_Export_Excel,
    OMT_Export,
    ASSIGN_OT_DIMENSIONS,
    ASSIGN_OT_EDGE_BANDING,
    PLACE_OT_OBJECTS,
    EXCEL_OT_CREATE_MATERIALS,
    EXCEL_OT_EXPORT,
    EXPORT_OT_OBJECTS_TIME
]
        
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        
    bpy.types.Scene.OMT_Export_tool = PointerProperty(type = OMT_Properties)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
        
    del bpy.types.Scene.OMT_Export_tool

if __name__ == "__main__":
    register()