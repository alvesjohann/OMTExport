
###########################################  Update Edge Banding Material Selection ###########################################

def UPDATED_PANEL_EDGE_WHITE_MATERIAL(self, context):
    SCENE = context.scene
    OMT_TOOL = SCENE.OMT_Export_tool
        
    if OMT_TOOL.PANEL_EDGE_BANDING_WHITE_MATERIAL:
        OMT_TOOL.PANEL_EDGE_BANDING_WOOD_MATERIAL = False
        OMT_TOOL.PANEL_EDGE_BANDING_BLACK_MATERIAL = False

def UPDATED_PANEL_EDGE_WOOD_MATERIAL(self, context):
    SCENE = context.scene
    OMT_TOOL = SCENE.OMT_Export_tool
        
    if OMT_TOOL.PANEL_EDGE_BANDING_WOOD_MATERIAL:
        OMT_TOOL.PANEL_EDGE_BANDING_WHITE_MATERIAL = False
        OMT_TOOL.PANEL_EDGE_BANDING_BLACK_MATERIAL = False

def UPDATED_PANEL_EDGE_BLACK_MATERIAL(self, context):
    SCENE = context.scene
    OMT_TOOL = SCENE.OMT_Export_tool
        
    if OMT_TOOL.PANEL_EDGE_BANDING_BLACK_MATERIAL:
        OMT_TOOL.PANEL_EDGE_BANDING_WHITE_MATERIAL = False
        OMT_TOOL.PANEL_EDGE_BANDING_WOOD_MATERIAL = False

###########################################  Update Edge Banding Thickness Selection ###########################################
    
def UPDATED_PANEL_EDGE_BANDING_22MM(self, context):
    SCENE = context.scene
    OMT_TOOL = SCENE.OMT_Export_tool
        
    if OMT_TOOL.PANEL_EDGE_BANDING_22MM:
        OMT_TOOL.PANEL_EDGE_BANDING_45MM = False
        OMT_TOOL.PANEL_EDGE_BANDING_100MM = False
    
def UPDATED_PANEL_EDGE_BANDING_45MM(self, context):
    SCENE = context.scene
    OMT_TOOL = SCENE.OMT_Export_tool
        
    if OMT_TOOL.PANEL_EDGE_BANDING_45MM:
        OMT_TOOL.PANEL_EDGE_BANDING_22MM = False
        OMT_TOOL.PANEL_EDGE_BANDING_100MM = False
    
def UPDATED_PANEL_EDGE_BANDING_100MM(self, context):
    SCENE = context.scene
    OMT_TOOL = SCENE.OMT_Export_tool
        
    if OMT_TOOL.PANEL_EDGE_BANDING_100MM:
        OMT_TOOL.PANEL_EDGE_BANDING_22MM = False
        OMT_TOOL.PANEL_EDGE_BANDING_45MM = False