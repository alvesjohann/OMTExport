from bpy.types import Panel

class OMT_Standards(Panel):
    bl_label = "Padrões"
    bl_idname = "OMT_PT_STANDARDS"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "OMT Export"

    def draw(self, context):
        LAYOUT = self.layout
        SCENE = context.scene
        OMT_TOOL = SCENE.OMT_Export_tool
    
        BOX = LAYOUT.box()
        ROW = BOX.row()
        ROW.prop(OMT_TOOL, "STANDARD_DISTANCE")
        #ROW = BOX.row()
        #ROW.prop(OMT_TOOL, "SEPARATION_MARK")
        
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

        BOX = LAYOUT.box()
        ROW = BOX.row()
        ROW.prop(OMT_TOOL, "OBJECT_TO_APPEND")

        ROW = BOX.row()
        ROW.prop(OMT_TOOL, "OBJECT_SIDE_SMALLER_BIGGER")
        ROW.prop(OMT_TOOL, "OBJECT_SIDE_LEFT_RIGHT")
        ROW.prop(OMT_TOOL, "OBJECT_SIDE_UP_DOWN")
        
        ROW = LAYOUT.row()
        ROW.operator("omt.place_objects")

class OMT_Legacy_Panel(Panel):
    bl_label = "excelMaterials (Legado)"
    bl_idname = "OMT_PT_EXCEL_MATERIALS_LEGACY"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "OMT Export"

    def draw(self, context):
        LAYOUT = self.layout
        SCENE = context.scene
        OMT_TOOL = SCENE.OMT_Export_tool

class OMT_Create_Materials_from_Excel(Panel):
    bl_label = "Criar Materiais"
    bl_idname = "OMT_PT_CREATE_MATERIALS"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "OMT Export"
    bl_parent_id = "OMT_PT_EXCEL_MATERIALS_LEGACY"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        LAYOUT = self.layout
        SCENE = context.scene
        OMT_TOOL = SCENE.OMT_Export_tool
        
        ROW = LAYOUT.row()
        ROW.prop(OMT_TOOL, "MATERIALS_EXCEL_FILE")
        
        ROW = LAYOUT.row()
        ROW.prop(OMT_TOOL, "MATERIAL_TAB")
        
        ROW = LAYOUT.row()
        ROW.prop(OMT_TOOL, "MATERIAL_COLUMN")
        
        ROW = LAYOUT.row()
        ROW.prop(OMT_TOOL, "MATERIAL_COLUMN_NAME")
        
        ROW = LAYOUT.row()
        ROW.operator("omt.create_materials")

class OMT_Export_Excel(Panel):
    bl_label = "Make Excel"
    bl_idname = "OMT_PT_EXPORT_EXCEL"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "OMT Export"
    bl_parent_id = "OMT_PT_EXCEL_MATERIALS_LEGACY"
    bl_options = {"DEFAULT_CLOSED"}

    def draw(self, context):
        LAYOUT = self.layout
        SCENE = context.scene
        OMT_TOOL = SCENE.OMT_Export_tool
        
        ROW = LAYOUT.row()
        ROW.prop(OMT_TOOL, "BLENDER_COST_FILE")
        
        ROW = LAYOUT.row()
        ROW.prop(OMT_TOOL, "BLENDER_COST_FILE_TAB")
        
        ROW = LAYOUT.row()
        ROW.prop(OMT_TOOL, "BLENDER_COST_FILE_ROW")
        
        ROW = LAYOUT.row()
        ROW.prop(OMT_TOOL, "BLENDER_COST_FILE_COLUMN")
        
        ROW = LAYOUT.row()
        ROW.prop(OMT_TOOL, "BLENDER_COST_FILE_MATERIALS_TAB")
        
        ROW = LAYOUT.row()
        ROW.operator("omt.export_excel")

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