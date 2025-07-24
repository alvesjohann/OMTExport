from bpy.types import Panel

class OMT_Measures(Panel):
    bl_label = "Sobrepor Medidas"
    bl_idname = "OMT_PT_MEASURES"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "OMT Export"

    def draw(self, context):
        LAYOUT = self.layout
        SCENE = context.scene
        OMT_TOOL = SCENE.OMT_Export_tool
    
        BOX = LAYOUT.box()
        ROW = BOX.row()
        ROW.prop(OMT_TOOL, "PANEL_MIN_DIMENSION")
        ROW.prop(OMT_TOOL, "PANEL_MIN_DIMENSION_BOOL")
        ROW = BOX.row()
        ROW.prop(OMT_TOOL, "PANEL_MAX_DIMENSION")
        ROW.prop(OMT_TOOL, "PANEL_MAX_DIMENSION_BOOL")
        
        ROW = LAYOUT.row()
        ROW.operator("omt.assign_dimensions")
        
        ROW = LAYOUT.row()
        ROW.operator("omt.remove_dimensions")

class OMT_Assign_Edge_Banding(Panel):
    bl_label = "Fita de Borda"
    bl_idname = "OMT_PT_ASSIGN_EDGE_BANDING"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "OMT Export"

    def draw(self, context):
        LAYOUT = self.layout
        SCENE = context.scene
        OMT_TOOL = SCENE.OMT_Export_tool
        
        BOX = LAYOUT.box()
        BOX.prop(OMT_TOOL, "PANEL_MIN_DIMENSION_EDGE_BANDING")
        BOX.prop(OMT_TOOL, "PANEL_MAX_DIMENSION_EDGE_BANDING")
        
        OUTSIDE_BOX = LAYOUT.box()
        INSIDE_BOX = OUTSIDE_BOX.box()
        ROW = INSIDE_BOX.row()
        ROW.prop(OMT_TOOL, "PANEL_EDGE_BANDING_WHITE_MATERIAL")
        ROW.prop(OMT_TOOL, "PANEL_EDGE_BANDING_BLACK_MATERIAL")
        ROW.prop(OMT_TOOL, "PANEL_EDGE_BANDING_WOOD_MATERIAL")
        
        INSIDE_BOX = OUTSIDE_BOX.box()
        ROW = INSIDE_BOX.row()
        ROW.prop(OMT_TOOL, "PANEL_EDGE_BANDING_22MM")
        ROW.prop(OMT_TOOL, "PANEL_EDGE_BANDING_45MM")
        ROW.prop(OMT_TOOL, "PANEL_EDGE_BANDING_100MM")
        
        ROW = LAYOUT.row()
        ROW.operator("omt.assign_edge_banding")

class OMT_Material_Edge_Banding(Panel):
    bl_label = "Definições de Material"
    bl_idname = "OMT_PT_MATERIAL_EDGE_BANDING"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "OMT Export"
    bl_parent_id = "OMT_PT_ASSIGN_EDGE_BANDING"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        LAYOUT = self.layout
        SCENE = context.scene
        OMT_TOOL = SCENE.OMT_Export_tool
        
        ROW = LAYOUT.row()
        ROW.prop(OMT_TOOL, "PANEL_EDGE_BANDING_MATERIAL")
        ROW = LAYOUT.row()
        ROW.prop(OMT_TOOL, "PANEL_EDGE_BANDING_NAME")

class OMT_Colors_Edge_Banding(Panel):
    bl_label = "Definições de Cores"
    bl_idname = "OMT_PT_COLOR_EDGE_BANDING"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "OMT Export"
    bl_parent_id = "OMT_PT_ASSIGN_EDGE_BANDING"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        LAYOUT = self.layout
        SCENE = context.scene
        OMT_TOOL = SCENE.OMT_Export_tool
        
        ROW = LAYOUT.row()
        ROW.prop(OMT_TOOL, "PANEL_EDGE_BANDING_BLACK_COLOR")
        ROW = LAYOUT.row()
        ROW.prop(OMT_TOOL, "PANEL_EDGE_BANDING_WHITE_COLOR")
        ROW = LAYOUT.row()
        ROW.prop(OMT_TOOL, "PANEL_EDGE_BANDING_WOOD_COLOR")
        
class OMT_Place_Objects(Panel):
    bl_label = "Adicionar Objetos"
    bl_idname = "OMT_PT_PLACE_OBJECTS"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "OMT Export"

    def draw(self, context):
        LAYOUT = self.layout
        SCENE = context.scene
        OMT_TOOL = SCENE.OMT_Export_tool
        
        ROW = LAYOUT.row()
        ROW.operator("omt.place_objects")
           
class OMT_Export(Panel):
    bl_label = "Exportar Objetos e Tempos"
    bl_idname = "OMT_PT_EXPORT"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "OMT Export"

    def draw(self, context):
        LAYOUT = self.layout
        SCENE = context.scene
        OMT_TOOL = SCENE.OMT_Export_tool
        
        ROW = LAYOUT.row()
        ROW.operator("omt.export_objects_time")     
'''        
CRIAR PAINEIS PARA DEFINIÇÕES DE TEMPO, SOLDA, ETC.
'''