import bpy
import math

from bpy.types import (
    Operator,
    Panel,
    PropertyGroup
)

from bpy.props import (
    BoolProperty,
    FloatProperty,
    IntProperty,
    PointerProperty,
    StringProperty
)

from .functions import *

###########################################  Properties ###########################################

class OMT_Properties(PropertyGroup):
    #DEFINIÇÕES GERAIS
    STANDARD_DISTANCE : FloatProperty(name = "Distãncia Padrão", default = 0.2)
    SEPARATION_MARK : StringProperty(name = "Separation Mark", default = " ")

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
    
    

###########################################  Panels ###########################################


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
class OMT_Export(Panel):
    bl_label = "Exportar Objetos e Tempos"
    bl_idname = "OMT_PT_EXPORT"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "OMT Export"

    def draw(self, context):'''
        


'''
CRIAR PAINEIS PARA DEFINIÇÕES DE TEMPO, SOLDA, ETC.
'''
        
        
########################################### Operators ###########################################


class ASSIGN_OT_DIMENSIONS(Operator):
    bl_label = "Atribuir"
    bl_idname = "omt.assign_dimensions"
    
    def execute(self, context):
        SCENE = context.scene
        OMT_TOOL = SCENE.OMT_Export_tool
        
        #CONVERTE FLOATS PARA INTS E METROS PARA MILÍMETROS
        LOCAL_PANEL_MIN_DIMENSION = int(round(OMT_TOOL.PANEL_MIN_DIMENSION*1000,0))
        LOCAL_PANEL_MAX_DIMENSION = int(round(OMT_TOOL.PANEL_MAX_DIMENSION*1000,0))
        
        #SE OS VALORES SÃO NULOS, DESCONSIDERA-OS
        if LOCAL_PANEL_MIN_DIMENSION == 0:
            OMT_TOOL.PANEL_MIN_DIMENSION_BOOL = False
        
        if LOCAL_PANEL_MAX_DIMENSION == 0:
            OMT_TOOL.PANEL_MAX_DIMENSION_BOOL = False
        
        #RETORNA SE TAMANHOS SÃO NULOS
        if LOCAL_PANEL_MIN_DIMENSION == 0 and  OMT_TOOL.PANEL_MAX_DIMENSION_BOOL == False:
            return {"FINISHED"}
        if LOCAL_PANEL_MAX_DIMENSION == 0 and  OMT_TOOL.PANEL_MIN_DIMENSION_BOOL == False:
            return {"FINISHED"}
        if LOCAL_PANEL_MIN_DIMENSION + LOCAL_PANEL_MAX_DIMENSION == 0:
            return {"FINISHED"}
        if OMT_TOOL.PANEL_MAX_DIMENSION_BOOL == False and OMT_TOOL.PANEL_MIN_DIMENSION_BOOL == False:
            return {"FINISHED"}
        
        #ALTERA VALORES SE O LADO MENOR É MAIOR QUE O LADO MAIOR
        if LOCAL_PANEL_MIN_DIMENSION > LOCAL_PANEL_MAX_DIMENSION and OMT_TOOL.PANEL_MIN_DIMENSION_BOOL and OMT_TOOL.PANEL_MAX_DIMENSION_BOOL:
            CHANGE_MAX_MIN = OMT_TOOL.PANEL_MIN_DIMENSION
            OMT_TOOL.PANEL_MIN_DIMENSION = OMT_TOOL.PANEL_MAX_DIMENSION
            OMT_TOOL.PANEL_MAX_DIMENSION = CHANGE_MAX_MIN
            
            LOCAL_PANEL_MIN_DIMENSION = int(round(OMT_TOOL.PANEL_MIN_DIMENSION*1000,0))
            LOCAL_PANEL_MAX_DIMENSION = int(round(OMT_TOOL.PANEL_MAX_DIMENSION*1000,0))
        
        
        SELECTED_OBJECT_PANEL_MIN_DIMENSION = ""
        SELECTED_OBJECT_PANEL_MAX_DIMENSION = ""
        JUMP_AUTOMATION = False
        
        #CONFIRMAR STRING DE 4 DÍGITOS PARA O TAMANHO MENOR
        if OMT_TOOL.PANEL_MIN_DIMENSION_BOOL == False:
            SELECTED_OBJECT_PANEL_MIN_DIMENSION = ""
        elif LOCAL_PANEL_MIN_DIMENSION > 9999:
            SELECTED_OBJECT_PANEL_MIN_DIMENSION = "9999"
        elif LOCAL_PANEL_MIN_DIMENSION < 10:
            SELECTED_OBJECT_PANEL_MIN_DIMENSION = "000" + str(LOCAL_PANEL_MIN_DIMENSION)
        elif LOCAL_PANEL_MIN_DIMENSION < 100:
            SELECTED_OBJECT_PANEL_MIN_DIMENSION = "00" + str(LOCAL_PANEL_MIN_DIMENSION)
        elif LOCAL_PANEL_MIN_DIMENSION < 1000:
            SELECTED_OBJECT_PANEL_MIN_DIMENSION = '0' + str(LOCAL_PANEL_MIN_DIMENSION)
        else:
            SELECTED_OBJECT_PANEL_MIN_DIMENSION = str(LOCAL_PANEL_MIN_DIMENSION)
            
        #CONFIRMAR STRING DE 4 DÍGITOS PARA O TAMANHO MAIOR 
        if OMT_TOOL.PANEL_MAX_DIMENSION_BOOL == False:
            SELECTED_OBJECT_PANEL_MAX_DIMENSION = ""
        elif LOCAL_PANEL_MAX_DIMENSION > 9999:
            SELECTED_OBJECT_PANEL_MAX_DIMENSION = "9999"
        elif LOCAL_PANEL_MAX_DIMENSION < 10:
            SELECTED_OBJECT_PANEL_MAX_DIMENSION = "000" + str(LOCAL_PANEL_MAX_DIMENSION)
        elif LOCAL_PANEL_MAX_DIMENSION < 100:
            SELECTED_OBJECT_PANEL_MAX_DIMENSION = "00" + str(LOCAL_PANEL_MAX_DIMENSION)
        elif LOCAL_PANEL_MAX_DIMENSION < 1000:
            SELECTED_OBJECT_PANEL_MAX_DIMENSION = '0' + str(LOCAL_PANEL_MAX_DIMENSION)
        else:
            SELECTED_OBJECT_PANEL_MAX_DIMENSION = str(LOCAL_PANEL_MAX_DIMENSION)        
        
        #DEFINIR TAMANHO PARA TODOS OS OBJETOS SELECIONADOS
        for SELECTED_OBJECT in bpy.context.selected_objects:
            SELECTED_OBJECT_STRING = SELECTED_OBJECT.name
            
            #PARA OBJETO QUE TEM TAMANHO DEFINIDO E AUTOMAÇÃO
            if OMT_TOOL.DIMENSION_AUTOMATION_CHAR in SELECTED_OBJECT_STRING:
                SELECTED_OBJECT_NAME, SELECTED_OBJECT_AUTOMATION = SELECTED_OBJECT_STRING.split(OMT_TOOL.DIMENSION_AUTOMATION_CHAR)
                
                if OMT_TOOL.AUTOMATION_CHAR in SELECTED_OBJECT_AUTOMATION:
                    SELECTED_OBJECT_AUTOMATION = SELECTED_OBJECT_AUTOMATION.split(OMT_TOOL.AUTOMATION_CHAR)[1]
                else:
                    SELECTED_OBJECT_AUTOMATION = ""
                    JUMP_AUTOMATION = True
            
            #PARA OBJETO QUE TEM AUTOMAÇÃO
            elif OMT_TOOL.AUTOMATION_CHAR in SELECTED_OBJECT_STRING:
                SELECTED_OBJECT_NAME, SELECTED_OBJECT_AUTOMATION = SELECTED_OBJECT_STRING.split(OMT_TOOL.AUTOMATION_CHAR)
            
            #PARA OBJETOS QUE NÃO TEM NEM TAMANHO NEM AUTOMAÇÃO
            else:
                SELECTED_OBJECT_NAME = SELECTED_OBJECT_STRING.split(".")[0]
                SELECTED_OBJECT_AUTOMATION = ""
                JUMP_AUTOMATION = True
            
            #EXCLUIR ESPAÇO EM BRANCO NO FINAL DO NOME DO OBJETO
            if SELECTED_OBJECT_NAME[-1] == " ":
                SELECTED_OBJECT_NAME = SELECTED_OBJECT_NAME[:-1]

            #ADICIONAR NUMERAÇÃO FINAL PARA O CASO DE OBJETOS COM NOMES IDÊNTICOS
            if "." in SELECTED_OBJECT_AUTOMATION:
                SELECTED_OBJECT_AUTOMATION = SELECTED_OBJECT_AUTOMATION.split(".")[0] + ".000"
            else:
                SELECTED_OBJECT_AUTOMATION = SELECTED_OBJECT_AUTOMATION + ".000"
                
            #ALTERAR NOME (SE O OBJETO NÃO POSSUI AUTOMAÇÃO, EXCLUI O CARACTER DE AUTOMAÇÃO)
            if JUMP_AUTOMATION:
                SELECTED_OBJECT_STRING = SELECTED_OBJECT_NAME + OMT_TOOL.DIMENSION_AUTOMATION_CHAR + SELECTED_OBJECT_PANEL_MIN_DIMENSION + OMT_TOOL.DIMENSION_AUTOMATION_SEPARATION_CHAR + SELECTED_OBJECT_PANEL_MAX_DIMENSION + SELECTED_OBJECT_AUTOMATION
    
            #ALTERAR NOME (SE O OBJETO POSSUI AUTOMAÇÃO)
            else:
                SELECTED_OBJECT_STRING = SELECTED_OBJECT_NAME + OMT_TOOL.DIMENSION_AUTOMATION_CHAR + SELECTED_OBJECT_PANEL_MIN_DIMENSION + OMT_TOOL.DIMENSION_AUTOMATION_SEPARATION_CHAR + SELECTED_OBJECT_PANEL_MAX_DIMENSION + " " + OMT_TOOL.AUTOMATION_CHAR + SELECTED_OBJECT_AUTOMATION
                
            #EXCLUIR "x" CASO MEDIDA MAIOR NÃO FOR SOBREPOSTA
            ALONE_X = OMT_TOOL.DIMENSION_AUTOMATION_SEPARATION_CHAR + " "
            if ALONE_X in SELECTED_OBJECT_STRING:
                SELECTED_OBJECT_STRING = SELECTED_OBJECT_STRING.replace(ALONE_X, " ")
                  
            SELECTED_OBJECT.name = SELECTED_OBJECT_STRING.replace(OMT_TOOL.DIMENSION_AUTOMATION_SEPARATION_CHAR + ".",".")
        
        return {"FINISHED"}


class REMOVE_OT_DIMENSIONS(Operator):
    bl_label = "Remover Medidas"
    bl_idname = "omt.remove_dimensions"
    
    def execute(self, context):
        SCENE = context.scene
        OMT_TOOL = SCENE.OMT_Export_tool
            
        #EXCLUIR MEDIDAS
        for SELECTED_OBJECT in bpy.context.selected_objects:
            SELECTED_OBJECT_STRING = SELECTED_OBJECT.name
            
            if OMT_TOOL.DIMENSION_AUTOMATION_CHAR in SELECTED_OBJECT_STRING:
                #SEPARA A AUTOMAÇÃO, SE ELA EXISTE, DO RESTO DA STRING
                if OMT_TOOL.AUTOMATION_CHAR in SELECTED_OBJECT_STRING:
                    SPLIT_NAME_AND_DIMENSIONS, SPLIT_AUTOMATION = SELECTED_OBJECT_STRING.split(OMT_TOOL.AUTOMATION_CHAR)
                    SPLIT_AUTOMATION = " " + OMT_TOOL.AUTOMATION_CHAR + SPLIT_AUTOMATION.split(".")[0] + ".000"
                    
                    #SEPARA O NOME DA SOBREPOSIÇÃO DE MEDIDAS
                    SPLIT_NAME, SPLIT_DIMENSION = SPLIT_NAME_AND_DIMENSIONS.split(OMT_TOOL.DIMENSION_AUTOMATION_CHAR)
                else:
                    SPLIT_NAME = SELECTED_OBJECT_STRING.split(OMT_TOOL.DIMENSION_AUTOMATION_CHAR)[0]
                    SPLIT_AUTOMATION = ".000"
                    
                #ALTERA NOME DO OBJETO    
                SELECTED_OBJECT_STRING = SPLIT_NAME + SPLIT_AUTOMATION
                SELECTED_OBJECT.name = SELECTED_OBJECT_STRING
                    
        return {"FINISHED"}


class ASSIGN_OT_EDGE_BANDING(Operator):
    bl_label = "Atribuir"
    bl_idname = "omt.assign_edge_banding"
    
    def execute(self, context):
        SCENE = context.scene
        OMT_TOOL = SCENE.OMT_Export_tool
        
        #DEFINIR COR DA FITA
        if OMT_TOOL.PANEL_EDGE_BANDING_WHITE_MATERIAL:
            EDGE_BANDING_MATERIAL = OMT_TOOL.EDGE_BANDING_WHITE_CHAR.upper()
        elif OMT_TOOL.PANEL_EDGE_BANDING_WOOD_MATERIAL:
            EDGE_BANDING_MATERIAL = OMT_TOOL.EDGE_BANDING_WOOD_CHAR.upper()
        elif OMT_TOOL.PANEL_EDGE_BANDING_BLACK_MATERIAL:
            EDGE_BANDING_MATERIAL = OMT_TOOL.EDGE_BANDING_BLACK_CHAR.upper()
        else:
            EDGE_BANDING_MATERIAL = '0'
        
        #DEFINIR LARGURA DA FITA
        if OMT_TOOL.PANEL_EDGE_BANDING_22MM:
            EDGE_BANDING_SIZE = OMT_TOOL.EDGE_BANDING_22MM_CHAR
        elif OMT_TOOL.PANEL_EDGE_BANDING_45MM:
            EDGE_BANDING_SIZE = OMT_TOOL.EDGE_BANDING_45MM_CHAR
        elif OMT_TOOL.PANEL_EDGE_BANDING_100MM:
            EDGE_BANDING_SIZE = OMT_TOOL.EDGE_BANDING_100MM_CHAR
        else:
            EDGE_BANDING_SIZE = '0'
            
        #RETORNAR CASO COR OU ESPESSURA DE FITA NÃO ESTEJAM SELECIONADAS
        if EDGE_BANDING_MATERIAL == '0' or EDGE_BANDING_SIZE == '0':
            return {"FINISHED"}
                
        #DEFINIR FITA DE BORDA PARA TODOS OS OBJETOS SELECIONADOS
        for SELECTED_OBJECT in bpy.context.selected_objects:
            SELECTED_OBJECT_STRING = SELECTED_OBJECT.name
            
            #PARA OBJETO QUE TEM AUTOMAÇÃO
            if OMT_TOOL.AUTOMATION_CHAR in SELECTED_OBJECT_STRING:
                SELECTED_OBJECT_NAME, SELECTED_OBJECT_AUTOMATIONS = SELECTED_OBJECT_STRING.split(OMT_TOOL.AUTOMATION_CHAR)
                
                #EXCLUIR AUTOMAÇÕES DA FITA DE BORDA SELECIONADA
                REPLACE_AUTOMATION = []
                SELECTED_SPLIT_STRING = SELECTED_OBJECT_AUTOMATIONS
                
                for INDEX in range(SELECTED_SPLIT_STRING.count(OMT_TOOL.SEPARATION_MARK)):
                    SELECTED_SPLIT_AUTOMATION, SELECTED_SPLIT_STRING = SELECTED_SPLIT_STRING.split(OMT_TOOL.SEPARATION_MARK,1)
                    
                    #REMOVER AUTOMAÇÃO DE FITA DE BORDA SE ELA SERÁ SOBREPOSTA
                    if SELECTED_SPLIT_AUTOMATION[0].lower() == OMT_TOOL.EDGE_BANDING:
                        if SELECTED_SPLIT_AUTOMATION[4].upper() == EDGE_BANDING_MATERIAL and SELECTED_SPLIT_AUTOMATION[3] == EDGE_BANDING_SIZE:
                            REPLACE_AUTOMATION.append(SELECTED_SPLIT_AUTOMATION)
                        
                for REPLACE_ITEM in REPLACE_AUTOMATION:
                    SELECTED_OBJECT_AUTOMATIONS = SELECTED_OBJECT_AUTOMATIONS.replace(REPLACE_ITEM + " ","")
            
            #PARA OBJETOS QUE NÃO TEM AUTOMAÇÃO
            else:
                SELECTED_OBJECT_NAME = SELECTED_OBJECT_STRING.split(".")[0]
                SELECTED_OBJECT_AUTOMATIONS = ""
                
                
            #ADICIONAR FITA DE BORDA NA AUTOMAÇÃO
            SELECTED_OBJECT_AUTOMATIONS = OMT_TOOL.EDGE_BANDING.upper() + str(OMT_TOOL.PANEL_MIN_DIMENSION_EDGE_BANDING) + str(OMT_TOOL.PANEL_MAX_DIMENSION_EDGE_BANDING) + EDGE_BANDING_SIZE + EDGE_BANDING_MATERIAL + " " + SELECTED_OBJECT_AUTOMATIONS
            
            
            #EXCLUIR ESPAÇO EM BRANCO NO FINAL DO NOME DO OBJETO
            if SELECTED_OBJECT_NAME[-1] == " ":
                SELECTED_OBJECT_NAME = SELECTED_OBJECT_NAME[:-1]
            
            #REMOVER FITA SE AMBAS AS DIMENSÕES ESTÃO ZEARADAS
            if "B00" in SELECTED_OBJECT_AUTOMATIONS:
                REMOVE_EDGE_BANDING =  "B00" + EDGE_BANDING_SIZE + EDGE_BANDING_MATERIAL + " "
                SELECTED_OBJECT_AUTOMATIONS = SELECTED_OBJECT_AUTOMATIONS.replace(REMOVE_EDGE_BANDING,"")
                
            #REMOVER ESPAÇOS DUPLOS    
            if "  " in SELECTED_OBJECT_AUTOMATIONS:
                SELECTED_OBJECT_AUTOMATIONS = SELECTED_OBJECT_AUTOMATIONS.replace("  "," ")
                
            #REMOVER ESPAÇO DEPOIS DO CARACTER DE AUTOMAÇÃO   
            if OMT_TOOL.AUTOMATION_CHAR + " " in SELECTED_OBJECT_AUTOMATIONS:
                SELECTED_OBJECT_AUTOMATIONS = SELECTED_OBJECT_AUTOMATIONS.replace(OMT_TOOL.AUTOMATION_CHAR + " ","")
            
            
            #ADICIONAR NUMERAÇÃO FINAL PARA O CASO DE OBJETOS COM NOMES IDÊNTICOS
            if " ." in SELECTED_OBJECT_AUTOMATIONS:
                SELECTED_OBJECT_AUTOMATIONS = SELECTED_OBJECT_AUTOMATIONS.split(" .")[0] + ".000"
            elif "." in SELECTED_OBJECT_AUTOMATIONS:
                SELECTED_OBJECT_AUTOMATIONS = SELECTED_OBJECT_AUTOMATIONS.split(".")[0] + ".000"
            else:
                SELECTED_OBJECT_AUTOMATIONS = SELECTED_OBJECT_AUTOMATIONS + ".000"
    
    
            #ALTERAR NOME DO OBJETO
            SELECTED_OBJECT_STRING = SELECTED_OBJECT_NAME + " " + OMT_TOOL.AUTOMATION_CHAR + SELECTED_OBJECT_AUTOMATIONS
                
            SELECTED_OBJECT.name = SELECTED_OBJECT_STRING.replace(" " + OMT_TOOL.AUTOMATION_CHAR + ".", ".")
        
        return {"FINISHED"}

class EXPORT_OT_OBJECTS_TIME(Operator):
    bl_label = "Exportar"
    bl_idname = "omt.export_objects_time"
    
    def execute(self, context):
        SCENE = context.scene
        OMT_TOOL = SCENE.OMT_Export_tool
        
        #DEFINIÇÕES GERAIS
        LIST_OF_OBJECTS = []
        LIST_OF_TIMES = []
        REPLACE_MATERIAL_STRING = [" @m2", " @M2", "@m2", "@M2", " @m", " @M", "@m", "@M", " @u", " @U", "@u", "@U"]
        
        #DEFINIÇÕES DE FITA DE BORDA
        EDGE_BANDING_MATERIAL = OMT_TOOL.PANEL_EDGE_BANDING_MATERIAL
        EDGE_BANDING_NAME = OMT_TOOL.PANEL_EDGE_BANDING_NAME

        EDGE_BANDING_BLACK_COLOR = OMT_TOOL.PANEL_EDGE_BANDING_BLACK_COLOR
        EDGE_BANDING_WHITE_COLOR = OMT_TOOL.PANEL_EDGE_BANDING_WHITE_COLOR
        EDGE_BANDING_WOOD_COLOR = OMT_TOOL.PANEL_EDGE_BANDING_WOOD_COLOR

        EDGE_BANDING = OMT_TOOL.EDGE_BANDING
        EDGE_BANDING_BLACK_CHAR = OMT_TOOL.EDGE_BANDING_BLACK_CHAR
        EDGE_BANDING_WHITE_CHAR = OMT_TOOL.EDGE_BANDING_WHITE_CHAR
        EDGE_BANDING_WOOD_CHAR = OMT_TOOL.EDGE_BANDING_WOOD_CHAR
        
        EDGE_BANDING_BLACK_22MM = 0
        EDGE_BANDING_BLACK_45MM = 0
        EDGE_BANDING_BLACK_100MM = 0

        EDGE_BANDING_WHITE_22MM = 0
        EDGE_BANDING_WHITE_45MM = 0
        EDGE_BANDING_WHITE_100MM = 0

        EDGE_BANDING_WOOD_22MM = 0
        EDGE_BANDING_WOOD_45MM = 0
        EDGE_BANDING_WOOD_100MM = 0

        #DEFINIÇÕES DE PARAFUSO
        SCREW_MATERIAL = OMT_TOOL.SCREW_MATERIAL
        SCREW_NAME = OMT_TOOL.SCREW_NAME
        SCREW_CHAR = OMT_TOOL.SCREW_CHAR

        SCREW_16MM_CHAR = OMT_TOOL.SCREW_16MM_CHAR
        SCREW_25MM_CHAR = OMT_TOOL.SCREW_25MM_CHAR
        SCREW_30MM_CHAR = OMT_TOOL.SCREW_30MM_CHAR
        SCREW_35MM_CHAR = OMT_TOOL.SCREW_35MM_CHAR
        SCREW_40MM_CHAR = OMT_TOOL.SCREW_40MM_CHAR
        SCREW_45MM_CHAR = OMT_TOOL.SCREW_45MM_CHAR
        SCREW_50MM_CHAR = OMT_TOOL.SCREW_50MM_CHAR

        SCREW_16MM = 0
        SCREW_25MM = 0
        SCREW_30MM = 0
        SCREW_35MM = 0
        SCREW_40MM = 0
        SCREW_45MM = 0
        SCREW_50MM = 0

        #DEFINIÇÕES DE CANTONEIRA ZAMAC
        ANGLE_BRACKET_ZAMAC_MATERIAL = OMT_TOOL.PANEL_ANGLE_BRACKET_ZAMAC_MATERIAL
        ANGLE_BRACKET_ZAMAC_NAME = OMT_TOOL.PANEL_ANGLE_BRACKET_ZAMAC_NAME
        ANGLE_BRACKET_ZAMAC_CHAR = OMT_TOOL.ANGLE_BRACKET_ZAMAC_CHAR
        
        ANGLE_BRACKET_ZAMAC = 0

        #DEFINIÇÕES DE PINTURA
        PAINTED_MDF_MATERIAL = OMT_TOOL.PAINTED_MDF_MATERIAL
        PAINTED_MDF_NAME = OMT_TOOL.PAINTED_MDF_NAME
        PAINTED_MDF_CHAR = OMT_TOOL.PAINTED_MDF_CHAR
        
        PAINTED_MDF = 0

        #DEFINIÇÕES DE MDF CANALETADO
        SLOTTED_MDF_MATERIAL = OMT_TOOL.SLOTTED_MDF_MATERIAL
        SLOTTED_MDF_NAME = OMT_TOOL.SLOTTED_MDF_NAME
        SLOTTED_MDF_CHAR = OMT_TOOL.SLOTTED_MDF_CHAR
        
        SLOTTED_MDF_SMALLER_SIDE_CHAR = OMT_TOOL.SLOTTED_MDF_SMALLER_SIDE_CHAR
        SLOTTED_MDF_BIGGER_SIDE_CHAR = OMT_TOOL.SLOTTED_MDF_BIGGER_SIDE_CHAR
        
        SLOTTED_MDF_DISTANCE = OMT_TOOL.SLOTTED_MDF_DISTANCE
        
        SLOTTED_MDF = 0

        #DEFINIÇÕES DE SOLDA (METAL)
        METAL_WELDING_CHAR = 'w'
        METAL_WELDING_TIME = 5
        METAL_WELDING = 0

        #DEFINIÇÕES DE DOBRA (METAL)
        METAL_BENDING_CHAR = 'd'
        METAL_BENDING_TIME = 5
        METAL_BENDING = 0

        #DEFINIÇÕES DE CORTE A LASER
        METAL_LASER_CUTTING_MATERIAL = "Corte Laser Metal"
        METAL_LASER_CUTTING_NAME = "Corte Laser"
        METAL_LASER_CUTTING_CHAR = 'c'

        METAL_LASER_CUTTING = 0
        
        #LISTAGEM DE TODOS OS OBJETOS
        for COLLECTION in bpy.data.collections:
            #EXCLUIR DA LISTA COLEÇÕES COM OBJETOS DE AUTOMAÇÃO
            if COLLECTION.name[0] == OMT_TOOL.AUTOMATION_CHAR:
                continue
            
            #MÉTODOS PARA OS OBJETOS EM TODAS AS OUTRAS COLEÇÕES
            for OBJECT in COLLECTION.all_objects:
                OBJECT_STRING = OBJECT.name.split(".")[0]
               
                #ENCONTRAR TODAS AS MEDIDAS
                THICKNESS = round(min(OBJECT.dimensions.x, OBJECT.dimensions.y, OBJECT.dimensions.z),3)
               
                MAX_DIMENSION = round(max(OBJECT.dimensions.x, OBJECT.dimensions.y, OBJECT.dimensions.z),3)
                MIN_DIMENSION = round(OBJECT.dimensions.x + OBJECT.dimensions.y + OBJECT.dimensions.z - THICKNESS - MAX_DIMENSION,3)
               
                #SOBREPOSIÇÃO DE DIMENSÕES
                if OMT_TOOL.DIMENSION_AUTOMATION_CHAR in OBJECT_STRING:
                    FORCED_DIMENSIONS = OBJECT_STRING.split(OMT_TOOL.DIMENSION_AUTOMATION_CHAR)[1].replace(" ","")
                   
                    try:
                        MIN_DIMENSION = float(FORCED_DIMENSIONS[:4])/1000
                    except:
                        pass
                    try:
                        FORCED_DIMENSIONS = OBJECT_STRING.lower().split(OMT_TOOL.DIMENSION_AUTOMATION_SEPARATION_CHAR)[1]
                        MAX_DIMENSION = float(FORCED_DIMENSIONS[:4])/1000
                    except:
                        pass
                   
                #DEFINE TIPO DE OBJETO
                MATERIAL = COLLECTION.name
                
                if OMT_TOOL.METER2_AUTOMATION_TYPE in MATERIAL.lower():
                    TYPE_OF_OBJECT = OMT_TOOL.METER2_AUTOMATION_TYPE
                    
                elif OMT_TOOL.LINEAR_METER_AUTOMATION_TYPE in MATERIAL.lower():
                    TYPE_OF_OBJECT = OMT_TOOL.LINEAR_METER_AUTOMATION_TYPE
                    
                elif OMT_TOOL.UNIT_AUTOMATION_TYPE in MATERIAL.lower():
                    TYPE_OF_OBJECT = OMT_TOOL.UNIT_AUTOMATION_TYPE
                   
                #CONVERSÃO DE STRINGS
                STRING_MIN_DIMENSION = str(MIN_DIMENSION).replace(".",",")
                STRING_MAX_DIMENSION = str(MAX_DIMENSION).replace(".",",")
               
                for STRING in REPLACE_MATERIAL_STRING:
                    MATERIAL = MATERIAL.replace(STRING,"")
           
                #SALVAR ITEM
                if TYPE_OF_OBJECT == OMT_TOOL.METER2_AUTOMATION_TYPE:
                    LIST_OF_OBJECTS.append(MATERIAL + "\t" + STRING_MIN_DIMENSION + "\t" + STRING_MAX_DIMENSION + "\t" + OBJECT_STRING)
           
                elif TYPE_OF_OBJECT == OMT_TOOL.LINEAR_METER_AUTOMATION_TYPE:
                    LIST_OF_OBJECTS.append(MATERIAL + "\tX\t" + STRING_MAX_DIMENSION + "\t" + OBJECT_STRING)
                   
                elif TYPE_OF_OBJECT == OMT_TOOL.UNIT_AUTOMATION_TYPE:
                    LIST_OF_OBJECTS.append(MATERIAL + "\tX\tX\t" + OBJECT_STRING)
                           
                #AUTOMAÇÕES
                if OMT_TOOL.AUTOMATION_CHAR in OBJECT_STRING:
                    AUTOMATION_STRING = OBJECT_STRING.split(OMT_TOOL.AUTOMATION_CHAR)[1]
                    AUTOMATION = []
                   
                   
                    #SEPARAR AUTOMAÇÕES
                    for INDEX in range(AUTOMATION_STRING.count(OMT_TOOL.SEPARATION_MARK)):
                        SPLIT_AUTOMATION, SPLIT_STRING = AUTOMATION_STRING.split(OMT_TOOL.SEPARATION_MARK,1)
                       
                        AUTOMATION.append(SPLIT_AUTOMATION)
                        AUTOMATION_STRING = SPLIT_STRING
                       
                    if "." in AUTOMATION_STRING:
                        AUTOMATION.append(AUTOMATION_STRING.split(".")[0])
                    else:
                        AUTOMATION.append(AUTOMATION_STRING)
                   
                    #IMPLEMENTAR AUTOMAÇÕES
                    for ITEM in AUTOMATION:
                        ITEM_AUTOMATION = ITEM[0].lower()
                        #FITA DE BORDA
                        if ITEM_AUTOMATION == EDGE_BANDING:
                            EDGE_BANDING_SMALLER_SIDE = int(ITEM[1])*MIN_DIMENSION
                            EDGE_BANDING_LARGER_SIDE = int(ITEM[2])*MAX_DIMENSION
                            EDGE_BANDING_TOTAL_SIZE = EDGE_BANDING_SMALLER_SIDE + EDGE_BANDING_LARGER_SIDE
                           
                           
                            EDGE_BANDING_THICKNESS = int(ITEM[3])
                            COLOR = ITEM[4].lower()
                           
                            if COLOR == EDGE_BANDING_WOOD_CHAR:
                                COLOR = EDGE_BANDING_WOOD_COLOR
                            elif COLOR == EDGE_BANDING_WHITE_CHAR:
                                COLOR = EDGE_BANDING_WHITE_COLOR
                            elif COLOR == EDGE_BANDING_BLACK_CHAR:
                                COLOR = EDGE_BANDING_BLACK_COLOR
                            else:
                                break
                               
                            if EDGE_BANDING_THICKNESS == 1 and COLOR == EDGE_BANDING_WOOD_COLOR:
                                EDGE_BANDING_WOOD_100MM += EDGE_BANDING_TOTAL_SIZE
                            elif EDGE_BANDING_THICKNESS == 2 and COLOR == EDGE_BANDING_WOOD_COLOR:
                                EDGE_BANDING_WOOD_22MM += EDGE_BANDING_TOTAL_SIZE
                            elif EDGE_BANDING_THICKNESS == 4 and COLOR == EDGE_BANDING_WOOD_COLOR:
                                EDGE_BANDING_WOOD_45MM += EDGE_BANDING_TOTAL_SIZE
                               
                            elif EDGE_BANDING_THICKNESS == 1 and COLOR == EDGE_BANDING_WHITE_COLOR:
                                EDGE_BANDING_WHITE_100MM += EDGE_BANDING_TOTAL_SIZE
                            elif EDGE_BANDING_THICKNESS == 2 and COLOR == EDGE_BANDING_WHITE_COLOR:
                                EDGE_BANDING_WHITE_22MM += EDGE_BANDING_TOTAL_SIZE
                            elif EDGE_BANDING_THICKNESS == 4 and COLOR == EDGE_BANDING_WHITE_COLOR:
                                EDGE_BANDING_WHITE_45MM += EDGE_BANDING_TOTAL_SIZE
                           
                            elif EDGE_BANDING_THICKNESS == 1 and COLOR == EDGE_BANDING_BLACK_COLOR:
                                EDGE_BANDING_BLACK_100MM += EDGE_BANDING_TOTAL_SIZE
                            elif EDGE_BANDING_THICKNESS == 2 and COLOR == EDGE_BANDING_BLACK_COLOR:
                                EDGE_BANDING_BLACK_22MM += EDGE_BANDING_TOTAL_SIZE
                            elif EDGE_BANDING_THICKNESS == 4 and COLOR == EDGE_BANDING_BLACK_COLOR:
                                EDGE_BANDING_BLACK_45MM += EDGE_BANDING_TOTAL_SIZE
                            else:
                                break
                       
                        #PARAFUSO    
                        elif ITEM_AUTOMATION == SCREW_CHAR:
                            SCREW_AUTOMATION = ITEM[1:3]
                            
                            SCREW_MIN_DIMENSION = int(ITEM[3])
                            SCREW_MIN_DIMENSION = (MIN_DIMENSION/OMT_TOOL.STANDARD_DISTANCE)*SCREW_MIN_DIMENSION
                            
                            SCREW_MAX_DIMENSION = int(ITEM[4])
                            SCREW_MAX_DIMENSION = (MAX_DIMENSION/OMT_TOOL.STANDARD_DISTANCE)*SCREW_MAX_DIMENSION
                            
                            #PARAFUSO 16mm
                            if SCREW_AUTOMATION == SCREW_16MM_CHAR:
                                SCREW_16MM += SCREW_MIN_DIMENSION
                                SCREW_16MM += SCREW_MAX_DIMENSION
                           
                            #PARAFUSO 25mm
                            elif SCREW_AUTOMATION == SCREW_25MM_CHAR:
                                SCREW_25MM += SCREW_MIN_DIMENSION
                                SCREW_25MM += SCREW_MAX_DIMENSION
                           
                            #PARAFUSO 30mm
                            elif SCREW_AUTOMATION == SCREW_30MM_CHAR:
                                SCREW_30MM += SCREW_MIN_DIMENSION
                                SCREW_30MM += SCREW_MAX_DIMENSION
                           
                            #PARAFUSO 35mm
                            elif SCREW_AUTOMATION == SCREW_35MM_CHAR:
                                SCREW_35MM += SCREW_MIN_DIMENSION
                                SCREW_35MM += SCREW_MAX_DIMENSION
                           
                            #PARAFUSO 40mm
                            elif SCREW_AUTOMATION == SCREW_40MM_CHAR:
                                SCREW_40MM += SCREW_MIN_DIMENSION
                                SCREW_40MM += SCREW_MAX_DIMENSION
                           
                            #PARAFUSO 45mm
                            elif SCREW_AUTOMATION == SCREW_45MM_CHAR:
                                SCREW_45MM += SCREW_MIN_DIMENSION
                                SCREW_45MM += SCREW_MAX_DIMENSION
                           
                            #PARAFUSO 50mm
                            elif SCREW_AUTOMATION == SCREW_50MM_CHAR:
                                SCREW_50MM += SCREW_MIN_DIMENSION
                                SCREW_50MM += SCREW_MAX_DIMENSION
                       
                        #CANTONEIRA ZAMAC MDF    
                        elif ITEM_AUTOMATION == ANGLE_BRACKET_ZAMAC_CHAR:
                            ANGLE_BRACKET_ZAMAC_MIN_DIMENSION = int(ITEM[1])
                            ANGLE_BRACKET_ZAMAC += (MIN_DIMENSION/OMT_TOOL.STANDARD_DISTANCE)*ANGLE_BRACKET_ZAMAC_MIN_DIMENSION
                            
                            ANGLE_BRACKET_ZAMAC_MAX_DIMENSION = int(ITEM[2])
                            ANGLE_BRACKET_ZAMAC += (MAX_DIMENSION/OMT_TOOL.STANDARD_DISTANCE)*ANGLE_BRACKET_ZAMAC_MAX_DIMENSION
                       
                        #PINTURA MDF    
                        elif ITEM_AUTOMATION == PAINTED_MDF_CHAR:
                            PAINTED_MDF_SIDES = int(ITEM[1])
                            PAINTED_MDF += MIN_DIMENSION*MAX_DIMENSION*PAINTED_MDF_SIDES
                       
                        #CANALETADO    
                        elif ITEM_AUTOMATION == SLOTTED_MDF_CHAR:
                            SLOTTED_MDF += MIN_DIMENSION*MAX_DIMENSION
                            
                            SLOTTED_MDF_SIDE_CHAR = ITEM[1]
                            
                            SLOTTED_MDF_COLOR_CHAR = ITEM[3].lower()
                            
                            if SLOTTED_MDF_SIDE_CHAR == SLOTTED_MDF_SMALLER_SIDE_CHAR:
                                SLOTTED_MDF_SIDE = MIN_DIMENSION
                                SLOTTED_MDF_QUANT = int(round(MAX_DIMENSION/SLOTTED_MDF_DISTANCE,0))
                            elif SLOTTED_MDF_SIDE_CHAR == SLOTTED_MDF_BIGGER_SIDE_CHAR:
                                SLOTTED_MDF_SIDE = MAX_DIMENSION
                                SLOTTED_MDF_QUANT = int(round(MIN_DIMENSION/SLOTTED_MDF_DISTANCE,0))
                            
                            SLATWALL_INSERT_SIZE = SLOTTED_MDF_SIDE*SLOTTED_MDF_QUANT
                            
                            if SLOTTED_MDF_COLOR_CHAR == EDGE_BANDING_BLACK_CHAR:
                                EDGE_BANDING_BLACK_22MM += SLATWALL_INSERT_SIZE
                            elif SLOTTED_MDF_COLOR_CHAR == EDGE_BANDING_WOOD_CHAR:
                                EDGE_BANDING_WOOD_22MM += SLATWALL_INSERT_SIZE
                            elif SLOTTED_MDF_COLOR_CHAR == EDGE_BANDING_WHITE_CHAR:
                                EDGE_BANDING_WHITE_22MM += SLATWALL_INSERT_SIZE
                       
                        #TEMPO DE SOLDA
                        elif ITEM_AUTOMATION == METAL_WELDING_CHAR:
                            METAL_WELDING_MIN_DIMENSION = int(ITEM[1])
                            METAL_WELDING += (MIN_DIMENSION/STANDARD_DISTANCE)*METAL_WELDING_MIN_DIMENSION
                            
                            METAL_WELDING_MAX_DIMENSION = int(ITEM[2])
                            METAL_WELDING += (MAX_DIMENSION/STANDARD_DISTANCE)*METAL_WELDING_MAX_DIMENSION
                            
                            TIME_SECONDS += METAL_WELDING*METAL_WELDING_TIME
                       
                        #TEMPO DE DOBRA
                        elif ITEM_AUTOMATION == METAL_BENDING_CHAR:
                            METAL_BENDING = int(ITEM[1:3])
                            
                            OMT_TOOL.TIME_SECONDS += math.ceil(METAL_BENDING*METAL_BENDING_TIME)
                            METAL_BENDING = 0
                       
                        #TEMPO DE CORTE LASER 
                        elif ITEM_AUTOMATION == METAL_LASER_CUTTING_CHAR:
                            METAL_LASER_CUTTING += int(ITEM[1:5])
                       
                        #TEMPO DA PEÇA    
                        elif ITEM_AUTOMATION == OMT_TOOL.TIME_CHAR:
                            OMT_TOOL.TIME_SECONDS += int(ITEM[1:5])
                            
            #ADICIONAR TEMPO TOTAL DO MATERIAL À LISTA DE TEMPOS                
            if OMT_TOOL.TIME_SECONDS > 0:
                OMT_TOOL.TIME_HOURS = int(math.floor(OMT_TOOL.TIME_SECONDS/3600))
                OMT_TOOL.TIME_MINUTES = int(math.floor(OMT_TOOL.TIME_SECONDS/60) - OMT_TOOL.TIME_HOURS*60)
                OMT_TOOL.TIME_SECONDS = int(round(OMT_TOOL.TIME_SECONDS - OMT_TOOL.TIME_MINUTES*60 - OMT_TOOL.TIME_HOURS*3600,0))
                    
                LIST_OF_TIMES.append(MATERIAL + "\t" + str(OMT_TOOL.TIME_HOURS) + "\t" + str(OMT_TOOL.TIME_MINUTES) + "\t" + str(OMT_TOOL.TIME_SECONDS))
                
                OMT_TOOL.TIME_HOURS = 0
                OMT_TOOL.TIME_MINUTES = 0
                OMT_TOOL.TIME_SECONDS = 0
               
        #ADICIONAR NOVOS ITENS (M² E METRO LINEAR)
        NEW_LINES = []
        if EDGE_BANDING_BLACK_22MM > 0:
            NEW_LINES.append(EDGE_BANDING_MATERIAL + " " + EDGE_BANDING_BLACK_COLOR + " 22mm\tX\t" + str(round(EDGE_BANDING_BLACK_22MM,1)).replace(".",",") + "\t" + EDGE_BANDING_NAME + " 22mm")
        if EDGE_BANDING_BLACK_45MM > 0:
            NEW_LINES.append(EDGE_BANDING_MATERIAL + " " + EDGE_BANDING_BLACK_COLOR + " 45mm\tX\t" + str(round(EDGE_BANDING_BLACK_45MM,1)).replace(".",",") + "\t" + EDGE_BANDING_NAME + " 45mm")
        if EDGE_BANDING_BLACK_100MM > 0:
            NEW_LINES.append(EDGE_BANDING_MATERIAL + " " + EDGE_BANDING_BLACK_COLOR + " 100mm\tX\t" + str(round(EDGE_BANDING_BLACK_100MM,1)).replace(".",",") + "\t" + EDGE_BANDING_NAME + " 100mm")
                               
        if EDGE_BANDING_WHITE_22MM > 0:
            NEW_LINES.append(EDGE_BANDING_MATERIAL + " " + EDGE_BANDING_WHITE_COLOR + " 22mm\tX\t" + str(round(EDGE_BANDING_WHITE_22MM,1)).replace(".",",") + "\t" + EDGE_BANDING_NAME + " 22mm")
        if EDGE_BANDING_WHITE_45MM > 0:
            NEW_LINES.append(EDGE_BANDING_MATERIAL + " " + EDGE_BANDING_WHITE_COLOR + " 45mm\tX\t" + str(round(EDGE_BANDING_WHITE_45MM,1)).replace(".",",") + "\t" + EDGE_BANDING_NAME + " 45mm")
        if EDGE_BANDING_WHITE_100MM > 0:
            NEW_LINES.append(EDGE_BANDING_MATERIAL + " " + EDGE_BANDING_WHITE_COLOR + " 100mm\tX\t" + str(round(EDGE_BANDING_WHITE_100MM,1)).replace(".",",") + "\t" + EDGE_BANDING_NAME + " 100mm")

        if EDGE_BANDING_WOOD_22MM > 0:
            NEW_LINES.append(EDGE_BANDING_MATERIAL + " " + EDGE_BANDING_WOOD_COLOR + " 22mm\tX\t" + str(round(EDGE_BANDING_WOOD_22MM,1)).replace(".",",") + "\t" + EDGE_BANDING_NAME + " 22mm")
        if EDGE_BANDING_WOOD_45MM > 0:
            NEW_LINES.append(EDGE_BANDING_MATERIAL + " " + EDGE_BANDING_WOOD_COLOR + " 45mm\tX\t" + str(round(EDGE_BANDING_WOOD_45MM,1)).replace(".",",") + "\t" + EDGE_BANDING_NAME + " 45mm")
        if EDGE_BANDING_WOOD_100MM > 0:
            NEW_LINES.append(EDGE_BANDING_MATERIAL + " " + EDGE_BANDING_WOOD_COLOR + " 100mm\tX\t" + str(round(EDGE_BANDING_WOOD_100MM,1)).replace(".",",") + "\t" + EDGE_BANDING_NAME + " 100mm")
            
        if PAINTED_MDF > 0:
            NEW_LINES.append(PAINTED_MDF_MATERIAL + "\tX\t" + str(round(PAINTED_MDF,2)).replace(".",",") + "\t" + PAINTED_MDF_NAME)
            
        if SLOTTED_MDF > 0:
            NEW_LINES.append(SLOTTED_MDF_MATERIAL + "\tX\t" + str(round(SLOTTED_MDF,3)).replace(".",",") + "\t" + SLOTTED_MDF_NAME)
            
        if METAL_LASER_CUTTING > 0:
            #CONVERTER PARA MINUTOS
            METAL_LASER_CUTTING = math.ceil(METAL_LASER_CUTTING/60)
            
            NEW_LINES.append(METAL_LASER_CUTTING_MATERIAL + "\tX\t" + str(METAL_LASER_CUTTING).replace(".",",") + "\t" + METAL_LASER_CUTTING_NAME)

        LIST_OF_OBJECTS.extend(NEW_LINES)

        #EXCLUIR AUTOMAÇÕES DA LISTA
        for INDEX, OBJECT in enumerate(LIST_OF_OBJECTS):
            if OMT_TOOL.DIMENSION_AUTOMATION_CHAR in OBJECT:
                LIST_OF_OBJECTS[INDEX] = OBJECT.split(OMT_TOOL.DIMENSION_AUTOMATION_CHAR)[0]
            elif OMT_TOOL.AUTOMATION_CHAR in OBJECT:
                LIST_OF_OBJECTS[INDEX] = OBJECT.split(OMT_TOOL.AUTOMATION_CHAR)[0]

        #SOMAR ITENS IGUAIS NA LISTA
        SUMMED_LIST_OF_OBJECTS = []

        for OBJECT in LIST_OF_OBJECTS:
            NEW_OBJECT = OBJECT + "\t" + str(LIST_OF_OBJECTS.count(OBJECT))
           
            if NEW_OBJECT in SUMMED_LIST_OF_OBJECTS:
                continue
            else:
                SUMMED_LIST_OF_OBJECTS.append(NEW_OBJECT)
                
        #ADICIONAR NOVOS ITENS (UNITÁRIO)
        NEW_LINES = []
        if SCREW_16MM > 0:
            SCREW_16MM = str(int(round(SCREW_16MM,0)))
            NEW_LINES.append(SCREW_MATERIAL + SCREW_16MM_CHAR + "\tX\tX\t" + SCREW_NAME + "\t" + SCREW_16MM)
        if SCREW_25MM > 0:
            SCREW_25MM = str(int(round(SCREW_25MM,0)))
            NEW_LINES.append(SCREW_MATERIAL + SCREW_25MM_CHAR + "\tX\tX\t" + SCREW_NAME + "\t" + SCREW_25MM)
        if SCREW_30MM > 0:
            SCREW_30MM = str(int(round(SCREW_30MM,0)))
            NEW_LINES.append(SCREW_MATERIAL + SCREW_30MM_CHAR + "\tX\tX\t" + SCREW_NAME + "\t" + SCREW_30MM)
        if SCREW_35MM > 0:
            SCREW_35MM = str(int(round(SCREW_35MM,0)))
            NEW_LINES.append(SCREW_MATERIAL + SCREW_35MM_CHAR + "\tX\tX\t" + SCREW_NAME + "\t" + SCREW_35MM)
        if SCREW_45MM > 0:
            SCREW_45MM = str(int(round(SCREW_45MM,0)))
            NEW_LINES.append(SCREW_MATERIAL + SCREW_45MM_CHAR + "\tX\tX\t" + SCREW_NAME + "\t" + SCREW_45MM)
        if SCREW_50MM > 0:
            SCREW_50MM = str(int(round(SCREW_50MM,0)))
            NEW_LINES.append(SCREW_MATERIAL + SCREW_50MM_CHAR + "\tX\tX\t" + SCREW_NAME + "\t" + SCREW_50MM)
            
        if ANGLE_BRACKET_ZAMAC > 0:
            ANGLE_BRACKET_ZAMAC = int(math.ceil(ANGLE_BRACKET_ZAMAC))
            ANGLE_BRACKET_ZAMAC_SCREW = str(ANGLE_BRACKET_ZAMAC*2)
            NEW_LINES.append(ANGLE_BRACKET_ZAMAC_MATERIAL + "\tX\tX\t" + ANGLE_BRACKET_ZAMAC_NAME + "\t" + str(ANGLE_BRACKET_ZAMAC))
            NEW_LINES.append(SCREW_MATERIAL + SCREW_16MM_CHAR + "\tX\tX\t" + SCREW_NAME + "\t" + ANGLE_BRACKET_ZAMAC_SCREW)
            
        SUMMED_LIST_OF_OBJECTS.extend(NEW_LINES)
               
        #ENCONTRAR CAMINHO DO BLENDER
        if bpy.data.is_saved:
            BLENDER_PATH = bpy.path.abspath("//") #ENCONTRAR O CAMINHO DO .BLEND      
               
            #EXPORTAÇÃO DE PEÇAS, MATERIAIS E SERVIÇOS
            with open(BLENDER_PATH + "//" + OMT_TOOL.OBJECTS_FILE + ".txt", "w") as file:
                file.write(OMT_TOOL.OBJECTS_FILE_HEADER)
                for OBJECT in SUMMED_LIST_OF_OBJECTS:
                    file.write(OBJECT + "\n")
                   
            #EXPORTAÇÃO DE TEMPOS  
            with open(BLENDER_PATH + "//" + OMT_TOOL.TIME_FILE + ".txt", "w") as file:
                file.write(OMT_TOOL.TIME_FILE_HEADER)
                for TIME in LIST_OF_TIMES:
                    file.write(TIME + "\n")
        else:
            print('File not saved.')
    

        return {"FINISHED"}


###########################################  Registration ###########################################

classes = [
    OMT_Properties,
    OMT_Measures,
    OMT_Assign_Edge_Banding,
    OMT_Material_Edge_Banding,
    OMT_Colors_Edge_Banding,
    OMT_Export,
    ASSIGN_OT_DIMENSIONS,
    REMOVE_OT_DIMENSIONS,
    ASSIGN_OT_EDGE_BANDING,
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
    try:
        unregister()
    except:
        pass
    register()