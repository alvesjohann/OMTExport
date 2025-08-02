from bpy.types import PropertyGroup

from bpy.props import (
    BoolProperty,
    EnumProperty,
    FloatProperty,
    IntProperty,
    StringProperty
)

from .update_functions import *

class OMT_Properties(PropertyGroup):
    #DEFINIÇÕES GERAIS
    STANDARD_DISTANCE : FloatProperty(name = "Distância", subtype = "DISTANCE", unit = "LENGTH",  min = 0, default = 0.2)
    SEPARATION_MARK : StringProperty(name = "Split Mark", default = " ")

    #DEFINIÇÕES DE EIXO
    X_AXIS : IntProperty(name = "X Axis", default = 0)
    Y_AXIS : IntProperty(name = "Y Axis", default = 1)
    Z_AXIS : IntProperty(name = "Z Axis", default = 2)

    #DEFINIÇÕES DE EXPORTAÇÃO
    OBJECTS_FILE : StringProperty(name = "Exportação: Lista de Objetos", default = "Lista de Peças e Materiais")
    OBJECTS_FILE_HEADER : StringProperty(name = "Objects Header", default = "MATERIAL\tLARGURA\tCOMPRIMENTO\tNOME\tQUANTIDADE\n")
    
    #DEFINIÇÕES DE AUTOMAÇÃO
    AUTOMATION_CHAR : StringProperty(name = "Automation Char", default = '@')
    
    DIMENSION_AUTOMATION_CHAR : StringProperty(name = "Dimension Automation Char", default = '_')
    DIMENSION_AUTOMATION_SEPARATION_CHAR : StringProperty(name = "Dimension Automation Separation Char", default = 'x')
    
    METER2_AUTOMATION_TYPE : StringProperty(name = "Automation Type: m²", default = "@m2")
    LINEAR_METER_AUTOMATION_TYPE : StringProperty(name = "Automation Type: m", default = "@m")
    UNIT_AUTOMATION_TYPE : StringProperty(name = "Automation Type: unity", default = "@u")
    
    #DEFINIÇÕES DE TEMPO
    TIME_CHAR : StringProperty(name = "Time Char", default = 't')

    TIME_HOURS : IntProperty(name = "Hours", default = 0)
    TIME_MINUTES : IntProperty(name = "Minutes", default = 0)
    TIME_SECONDS : IntProperty(name = "Seconds", default = 0)

    TIME_FILE : StringProperty(name = "Exportação: Lista de Tempos", default = "Lista de Tempos")
    TIME_FILE_HEADER : StringProperty(name = "Time Header", default = "MATERIAL\tHORAS\tMINUTOS\tSEGUNDOS\n")
    
    #DEFINIÇÕES DE MEDIDAS
    PANEL_MIN_DIMENSION : FloatProperty(name = "Lado Menor", subtype = "DISTANCE", unit = "LENGTH", min = 0)
    PANEL_MIN_DIMENSION_BOOL : BoolProperty(name = "", default = True)
    PANEL_MAX_DIMENSION : FloatProperty(name = "Lado Maior", subtype = "DISTANCE", unit = "LENGTH", min = 0)
    PANEL_MAX_DIMENSION_BOOL : BoolProperty(name = "", default = True)
    
    #DEFINIÇÕES DE FITA DE BORDA
    EDGE_BANDING : StringProperty(name = "Edge Banding Char", default = 'b')
    
    EDGE_BANDING_BLACK_CHAR : StringProperty(name = "Edge Banding Black Char", default = 'p')
    EDGE_BANDING_WHITE_CHAR : StringProperty(name = "Edge Banding WhiteChar", default = 'b')
    EDGE_BANDING_WOOD_CHAR : StringProperty(name = "Edge Banding Wood Char", default = 'a')
    
    EDGE_BANDING_22MM_CHAR : StringProperty(name = "Edge Banding 22mm Char", default = '2')
    EDGE_BANDING_45MM_CHAR : StringProperty(name = "Edge Banding 45mm Char", default = '4')
    EDGE_BANDING_100MM_CHAR : StringProperty(name = "Edge Banding 100mm Char", default = '1')
    
    PANEL_MIN_DIMENSION_EDGE_BANDING : IntProperty(name = "Fita Lado Menor", default = 0, min = 0, max = 2)
    PANEL_MAX_DIMENSION_EDGE_BANDING : IntProperty(name = "Fita Lado Maior", default = 0, min = 0, max = 2)
    
    PANEL_EDGE_BANDING_WHITE_MATERIAL : BoolProperty(name = "Branca", default = True, update = UPDATED_PANEL_EDGE_WHITE_MATERIAL)
    PANEL_EDGE_BANDING_WOOD_MATERIAL : BoolProperty(name = "Madeira", default = False, update = UPDATED_PANEL_EDGE_WOOD_MATERIAL)
    PANEL_EDGE_BANDING_BLACK_MATERIAL : BoolProperty(name = "Preta", default = False, update = UPDATED_PANEL_EDGE_BLACK_MATERIAL)
    
    PANEL_EDGE_BANDING_MATERIAL : StringProperty(name = "Material", default = "Fita de Borda")
    PANEL_EDGE_BANDING_NAME : StringProperty(name = "Descrição", default = "Fita")

    PANEL_EDGE_BANDING_BLACK_COLOR : StringProperty(name = "Preta", default = "Preta")
    PANEL_EDGE_BANDING_WHITE_COLOR : StringProperty(name = "Branca", default = "Branca")
    PANEL_EDGE_BANDING_WOOD_COLOR : StringProperty(name = "Madeira", default = "Amadeirado")
    
    PANEL_EDGE_BANDING_22MM : BoolProperty(name = "22mm", default = True, update = UPDATED_PANEL_EDGE_BANDING_22MM)
    PANEL_EDGE_BANDING_45MM : BoolProperty(name = "45mm", default = False, update = UPDATED_PANEL_EDGE_BANDING_45MM)
    PANEL_EDGE_BANDING_100MM : BoolProperty(name = "100mm", default = False, update = UPDATED_PANEL_EDGE_BANDING_100MM)
    
    #DEFINIÇÕES DE PARAFUSO
    SCREW_MATERIAL : StringProperty(name = "Material", default = "Paraf. Chato PHS 4x")
    SCREW_NAME : StringProperty(name = "Descrição", default = "Parafuso")
    SCREW_CHAR : StringProperty(name = "Screw Char", default = 's')

    SCREW_16MM_CHAR : StringProperty(name = "16mm Screw Char", default = "16")
    SCREW_25MM_CHAR : StringProperty(name = "25mm Screw Char", default = "25")
    SCREW_30MM_CHAR : StringProperty(name = "30mm Screw Char", default = "30")
    SCREW_35MM_CHAR : StringProperty(name = "35mm Screw Char", default = "35")
    SCREW_40MM_CHAR : StringProperty(name = "40mm Screw Char", default = "40")
    SCREW_45MM_CHAR : StringProperty(name = "45mm Screw Char", default = "45")
    SCREW_50MM_CHAR : StringProperty(name = "50mm Screw Char", default = "50")
    
    #DEFINIÇÕES DE CANTONEIRA ZAMAC
    ANGLE_BRACKET_ZAMAC_CHAR : StringProperty(name = "Angle Bracket Zamac Char", default = 'z')
    
    PANEL_ANGLE_BRACKET_ZAMAC_MATERIAL : StringProperty(name = "Material", default = "Cantoneira 13x13mm 2 Furos")
    PANEL_ANGLE_BRACKET_ZAMAC_NAME : StringProperty(name = "Descrição", default = "Cantoneira")
    
    #DEFINIÇÕES DE PINTURA
    PAINTED_MDF_MATERIAL : StringProperty(name = "Material", default = "Pintura Projetta MDF")
    PAINTED_MDF_NAME : StringProperty(name = "Descrição", default = "Pintura")
    PAINTED_MDF_CHAR : StringProperty(name = "Painted MDF Char", default = 'p')

    #DEFINIÇÕES DE MDF CANALETADO
    SLOTTED_MDF_MATERIAL : StringProperty(name = "Material", default = "Canaletagem MDF")
    SLOTTED_MDF_NAME : StringProperty(name = "Descrição", default = "Canaletagem")
    SLOTTED_MDF_CHAR : StringProperty(name = "Slotted MDF Char",  default = 'f')
    
    SLOTTED_MDF_SMALLER_SIDE_CHAR : StringProperty(name = "Slotted MDF Smaller Side Char",  default = '0')
    SLOTTED_MDF_BIGGER_SIDE_CHAR : StringProperty(name = "Slotted MDF Bigger Side Char",  default = '1')
    
    SLOTTED_MDF_DISTANCE : FloatProperty(name = "Distância", subtype = "DISTANCE", unit = "LENGTH", min = 1, default = 0.11)

    #DEFINIÇÕES DE SOLDA (METAL)
    METAL_WELDING_CHAR : StringProperty(name = "Metal Welding Char",  default = 'w')
    METAL_WELDING_TIME : IntProperty(name = "Tempo de Solda", default = 5, min = 0)

    #DEFINIÇÕES DE DOBRA (METAL)
    METAL_BENDING_CHAR : StringProperty(name = "Metal Bending Char",  default = 'd')
    METAL_BENDING_TIME : IntProperty(name = "Tempo de Dobra", default = 5, min = 0)

    #DEFINIÇÕES DE CORTE A LASER
    METAL_LASER_CUTTING_MATERIAL : StringProperty(name = "Material",  default = "Corte Laser Metal")
    METAL_LASER_CUTTING_NAME : StringProperty(name = "Descrição", default = "Corte Laser")
    METAL_LASER_CUTTING_CHAR : StringProperty(name = "Metal Laser Char",  default = 'c')

    #DEFINIÇÕES DE ADIÇÃO DE OBJETOS
    ACCESSORIES_PATH : StringProperty(name = "Accessories Path",  default = "\\assets\\accessories.blend")

    OBJECT_TO_APPEND : EnumProperty(name = "",
                               default = "Cantoneira",
                               items = [("Cantoneira", "Cantoneira", "Cantoneira L 13x13mm Zamac.")]
                               )

    OBJECT_SIDE_SMALLER_BIGGER : EnumProperty(name = "Lado",
                               default = "SMALLER",
                               items = [("SMALLER", "Menor", "Adicionar objetos ao lado menor."),
                                        ("BIGGER", "Maior", "Adicionar objetos ao lado maior.")]
                               )
    OBJECT_SIDE_LEFT_RIGHT : EnumProperty(name = "",
                               default = "LEFT",
                               items = [("LEFT", "Esquerdo", "Adicionar objetos à esquerda."),
                                        ("RIGHT", "Direito", "Adicionar objetos à direita.")]
                               )
    OBJECT_SIDE_UP_DOWN : EnumProperty(name = "",
                               default = "DOWN",
                               items = [("UP", "Superior", "Adicionar objetos no topo."),
                                        ("DOWN", "Inferior", "Adicionar objetos na base.")]
                               )


    #DEFINIÇÕES DE EXCEL
    USE_BLENDER_MATERIALS : BoolProperty(name = "Usar Materiais do Blender", default = True, description = "Quando desmarcado, usará os nomes das coleções")

    MATERIAL_TAB : StringProperty(name = "Tab", default = "Dados")
    MATERIAL_COLUMN : StringProperty(name = "Col.", default = "A")
    MATERIAL_COLUMN_NAME : StringProperty(name = "Col. Materiais", default = "Produtos") 
    MATERIALS_EXCEL_FILE: StringProperty(name = "Excel", subtype="FILE_PATH", default = "")

    BLENDER_COST_FILE: StringProperty(name = "Excel", subtype="FILE_PATH", default = "")
    BLENDER_COST_FILE_TAB: StringProperty(name = "Export Tab", default = "BlenderExport")
    BLENDER_COST_FILE_ROW : IntProperty(name = "Start Row", default = 6)
    BLENDER_COST_FILE_COLUMN: IntProperty(name = "Start Column", default = 0)
    BLENDER_COST_FILE_MATERIALS_TAB: StringProperty(name = "Banco Tab", default = "Banco")
