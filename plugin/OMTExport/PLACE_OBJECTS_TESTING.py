import bpy
import math

#DEFINIÇÕES
X_AXIS = 0
Y_AXIS = 1
Z_AXIS = 2

STANDARD_DISTANCE = 0.2
MIN_AMOUNT = 2
STANDARD_OFFSET = 0.0

ACCESSORIES_PATH = "//assets/accessories.blend"
IMPORTED_OBJECT_NAME = "Cantoneira"
LINK = False

def ACTIVE_OBJECT_DIMENSIONS_LIST():

    #OBJETO SELECIONADO
    ACTIVE_OBJECT = bpy.context.active_object

    #APLICAR TRANSFORMAÇÕES
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

    #SEPARAR MEDIDAS
    ACTIVE_OBJECT_X = round(ACTIVE_OBJECT.dimensions.x,3)
    ACTIVE_OBJECT_Y = round(ACTIVE_OBJECT.dimensions.y,3)
    ACTIVE_OBJECT_Z = round(ACTIVE_OBJECT.dimensions.z,3)
    
    return [ACTIVE_OBJECT_X, ACTIVE_OBJECT_Y, ACTIVE_OBJECT_Z]

def ACTIVE_OBJECT_WORLD_MATRIX():
    
    return bpy.context.active_object.matrix_world

def ACTIVE_OBJECT_VERTICES():
    
    return bpy.context.active_object.data.vertices

def OBJECT_DIMENSIONS(DIMENSIONS, MAKE_DIMENSION = False):

    if MAKE_DIMENSION:
        DIMENSIONS = ACTIVE_OBJECT_DIMENSIONS_LIST()
    
    #SEPARAR DIMENSÕES
    ACTIVE_OBJECT_X = DIMENSIONS[0]
    ACTIVE_OBJECT_Y = DIMENSIONS[1]
    ACTIVE_OBJECT_Z = DIMENSIONS[2]
    
    return ACTIVE_OBJECT_X, ACTIVE_OBJECT_Y, ACTIVE_OBJECT_Z


def OBJECT_SIDE_DIMENSION(DIMENSIONS, MATH_OPERATION = "MIN"):
    #SEPARAR DIMENSÕES
    ACTIVE_OBJECT_X, ACTIVE_OBJECT_Y, ACTIVE_OBJECT_Z = OBJECT_DIMENSIONS(DIMENSIONS)
    
    if MATH_OPERATION == "MIN":
        return min(ACTIVE_OBJECT_X, ACTIVE_OBJECT_Y, ACTIVE_OBJECT_Z)
    elif MATH_OPERATION == "MAX":
        return max(ACTIVE_OBJECT_X, ACTIVE_OBJECT_Y, ACTIVE_OBJECT_Z)
    
    MAX_DIMENSION = max(ACTIVE_OBJECT_X, ACTIVE_OBJECT_Y, ACTIVE_OBJECT_Z)
    MIN_DIMENSION = min(ACTIVE_OBJECT_X, ACTIVE_OBJECT_Y, ACTIVE_OBJECT_Z)
    
    MED_DIMENSION = round(ACTIVE_OBJECT_X + ACTIVE_OBJECT_Y + ACTIVE_OBJECT_Z - MIN_DIMENSION - MAX_DIMENSION,3)
    
    return MED_DIMENSION
    
def OBJECT_SIDE_AXIS(SIDE_SIZE, DIMENSIONS):
    #SEPARAR DIMENSÕES
    ACTIVE_OBJECT_X, ACTIVE_OBJECT_Y, ACTIVE_OBJECT_Z = OBJECT_DIMENSIONS(DIMENSIONS)
    
    #ENCONTRAR EIXO
    if SIDE_SIZE == ACTIVE_OBJECT_X:
        return X_AXIS
    elif SIDE_SIZE == ACTIVE_OBJECT_Y:
        return Y_AXIS

    return Z_AXIS

def AMOUNT_OF_OBJECTS(DISTANCE, MIN = MIN_AMOUNT, GAP = STANDARD_DISTANCE):
    
    AMOUNT = int(round((DISTANCE)/GAP,0))
    
    if AMOUNT < MIN:
        return MIN
        
    return AMOUNT

def OFFSET(DISTANCE, AMOUNT, GAP = STANDARD_DISTANCE):
    
    return (DISTANCE - (AMOUNT - 1) * GAP)/2

def ADD_CONSTANT_ARRAY(OBJECT, AMOUNT, ARRAY_NAME = "Array", DISTANCE = 0.2):

    OBJECT_ARRAY_MODIFIER = OBJECT.modifiers.new(name = ARRAY_NAME, type = 'ARRAY')
    OBJECT_ARRAY_MODIFIER.use_relative_offset = False
    OBJECT_ARRAY_MODIFIER.use_constant_offset = True
    OBJECT_ARRAY_MODIFIER.constant_offset_displace = (DISTANCE, 0.0, 0.0)            

    OBJECT_ARRAY_MODIFIER.count = AMOUNT

def SEPARATE_ARRAY_OBJECTS(OBJECT, ARRAY_NAME):       

    #OBJETO SELECIONADO
    ACTIVE_OBJECT = bpy.context.active_object
    #ALTERAR PARA OBJETO IMPORTADO
    bpy.context.view_layer.objects.active = OBJECT
    #APLICAR MODIFICADOR
    bpy.ops.object.modifier_apply(modifier = ARRAY_NAME)

    #SEPARAR OBJETOS
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.separate(type='LOOSE')
    bpy.ops.object.editmode_toggle()
    bpy.ops.object.select_all(action='DESELECT')
    
    #SELECIONAR OBJETO ORIGINAL
    bpy.context.view_layer.objects.active = ACTIVE_OBJECT
    ACTIVE_OBJECT.select_set(True)

def CREATE_ARRAY_OBJECTS(OBJECTS, LOCATION_XYZ, SCALE_XYZ, ROTATION_AXIS, ROTATION, AMOUNT, ARRAY_NAME = "Array", DISTANCE = 0.2):

    for OBJECT in OBJECTS:
        if OBJECT is not None:
            bpy.context.scene.collection.objects.link(OBJECT)
            
            #MOVER OBJETO PARA O PONTO CORRETO
            OBJECT_TO_MOVE = bpy.data.objects[OBJECT.name]
            
            #PONTO DE INÍCIO
            OBJECT_TO_MOVE.location = LOCATION_XYZ
            OBJECT_TO_MOVE.scale = SCALE_XYZ
            OBJECT_TO_MOVE.rotation_euler[ROTATION_AXIS] = ROTATION
            
            #CRIAR ARRAY COM CONSTANT OFFSET
            ADD_CONSTANT_ARRAY(OBJECT_TO_MOVE, AMOUNT, ARRAY_NAME, DISTANCE)
            
            #APLICAR MODIFICADOR E SEPARAR PEÇAS
            SEPARATE_ARRAY_OBJECTS(OBJECT_TO_MOVE, ARRAY_NAME)
    
def IMPORT_OBJECTS(PATH, OBJECT_NAME, IS_LINK = False):

    with bpy.data.libraries.load(PATH, link = IS_LINK) as (data_from, data_to):
        data_to.objects = [name for name in data_from.objects if name.startswith(OBJECT_NAME)]
        
    return data_to.objects
    
def RETURN_VERTICES_POSITIONING():

    OBJECT_DIMENSIONS = ACTIVE_OBJECT_DIMENSIONS_LIST()
    
    THICKNESS = OBJECT_SIDE_DIMENSION(OBJECT_DIMENSIONS, MATH_OPERATION = "MIN")
    THICKNESS_SIDE_AXIS = OBJECT_SIDE_AXIS(THICKNESS, OBJECT_DIMENSIONS)
    
    BIGGER_SIDE = OBJECT_SIDE_DIMENSION(OBJECT_DIMENSIONS, MATH_OPERATION = "MAX")
    BIGGER_SIDE_AXIS = OBJECT_SIDE_AXIS(BIGGER_SIDE, OBJECT_DIMENSIONS)
    
    SMALLER_SIDE = OBJECT_SIDE_DIMENSION(OBJECT_DIMENSIONS, MATH_OPERATION = "MED")
    SMALLER_SIDE_AXIS = OBJECT_SIDE_AXIS(SMALLER_SIDE, OBJECT_DIMENSIONS)
        
    #ENCONTRAR MATRIZ GLOBAL
    WORLD_MATRIX = ACTIVE_OBJECT_WORLD_MATRIX()
    #LISTA DE VERTICES DO OBJETO SELECIONADO
    OBJECT_VERTICES = ACTIVE_OBJECT_VERTICES()

    #ENCONTRAR INÍCIO E FIM DE CADA DIMENSÃO
    for VERTEX in OBJECT_VERTICES:
        INDEX = VERTEX.index
        WORLD_VERTEX = WORLD_MATRIX @ VERTEX.co
        
        WORLD_VERTEX_X = WORLD_VERTEX[0]
        WORLD_VERTEX_Y = WORLD_VERTEX[1]
        WORLD_VERTEX_Z = WORLD_VERTEX[2]
        
        if INDEX == 0:
            SMALLER_X = WORLD_VERTEX_X
            SMALLER_Y = WORLD_VERTEX_Y
            SMALLER_Z = WORLD_VERTEX_Z
            
            BIGGER_X = WORLD_VERTEX_X
            BIGGER_Y = WORLD_VERTEX_Y
            BIGGER_Z = WORLD_VERTEX_Z
        
        else:
            if WORLD_VERTEX_X < SMALLER_X:
                SMALLER_X = WORLD_VERTEX_X
            elif WORLD_VERTEX_X > BIGGER_X:
                BIGGER_X = WORLD_VERTEX_X
                
            if WORLD_VERTEX_Y < SMALLER_Y:
                SMALLER_Y = WORLD_VERTEX_Y
            elif WORLD_VERTEX_Y > BIGGER_Y:
                BIGGER_Y = WORLD_VERTEX_Y
                
            if WORLD_VERTEX_Z < SMALLER_Z:
                SMALLER_Z = WORLD_VERTEX_Z
            elif WORLD_VERTEX_Z > BIGGER_Z:
                BIGGER_Z = WORLD_VERTEX_Z

    #DEFINIR INÍCIO E FINAL GLOBAL DO LADO MENOR E MAIOR
    if THICKNESS_SIDE_AXIS == X_AXIS:
        THICKNESS_START = SMALLER_X
        THICKNESS_END = BIGGER_X
        #CASO LADOR MAIOR Y E LADO MENOR Z
        if BIGGER_SIDE_AXIS == Y_AXIS:
            SMALLER_SIDE_START = SMALLER_Z
            SMALLER_SIDE_END = BIGGER_Z
            
            BIGGER_SIDE_START = SMALLER_Y
            BIGGER_SIDE_END = BIGGER_Y
        #CASO LADOR MAIOR Z E LADO MENOR Y
        else:
            SMALLER_SIDE_START = SMALLER_Y
            SMALLER_SIDE_END = BIGGER_Y
            
            BIGGER_SIDE_START = SMALLER_Z
            BIGGER_SIDE_END = BIGGER_Z
            
    elif THICKNESS_SIDE_AXIS == Y_AXIS:
        THICKNESS_START = SMALLER_Y
        THICKNESS_END = BIGGER_Y
        #CASO LADOR MAIOR Z E LADO MENOR X
        if BIGGER_SIDE_AXIS == Z_AXIS:
            SMALLER_SIDE_START = SMALLER_X
            SMALLER_SIDE_END = BIGGER_X
            
            BIGGER_SIDE_START = SMALLER_Z
            BIGGER_SIDE_END = BIGGER_Z
        #CASO LADOR MAIOR X E LADO MENOR Z
        else:
            SMALLER_SIDE_START = SMALLER_Z
            SMALLER_SIDE_END = BIGGER_Z
            
            BIGGER_SIDE_START = SMALLER_X
            BIGGER_SIDE_END = BIGGER_X
            
    elif THICKNESS_SIDE_AXIS == Z_AXIS:
        THICKNESS_START = SMALLER_Z
        THICKNESS_END = BIGGER_Z
        #CASO LADOR MAIOR X E LADO MENOR Y
        if BIGGER_SIDE_AXIS == X_AXIS:
            SMALLER_SIDE_START = SMALLER_Y
            SMALLER_SIDE_END = BIGGER_Y
            
            BIGGER_SIDE_START = SMALLER_X
            BIGGER_SIDE_END = BIGGER_X
        #CASO LADOR MAIOR Y E LADO MENOR X
        else:
            SMALLER_SIDE_START = SMALLER_X
            SMALLER_SIDE_END = BIGGER_X
            
            BIGGER_SIDE_START = SMALLER_Y
            BIGGER_SIDE_END = BIGGER_Y
    
    OBJECT_POSITIONS_DICT = {
        "SMALLER_SIDE_AXIS" : SMALLER_SIDE_AXIS,
        "SMALLER_SIDE_START" : SMALLER_SIDE_START,
        "SMALLER_SIDE_END" : SMALLER_SIDE_END,
        "BIGGER_SIDE_AXIS" : BIGGER_SIDE_AXIS,
        "BIGGER_SIDE_START" : BIGGER_SIDE_START,
        "BIGGER_SIDE_END" : BIGGER_SIDE_END,
        "THICKNESS_SIDE_AXIS" : THICKNESS_SIDE_AXIS,
        "THICKNESS_START" : THICKNESS_START,
        "THICKNESS_END" : THICKNESS_END,
        "SMALLER_SIDE" : SMALLER_SIDE,
        "BIGGER_SIDE" : BIGGER_SIDE,
        "THICKNESS" : THICKNESS
    }
    
    return OBJECT_POSITIONS_DICT

def APPEND_OBJECTS(
        SMALLER_SIDE_AXIS,
        SMALLER_SIDE_START,
        SMALLER_SIDE_END,
        BIGGER_SIDE_AXIS,
        BIGGER_SIDE_START,
        BIGGER_SIDE_END,
        THICKNESS_SIDE_AXIS,
        THICKNESS_START,
        THICKNESS_END,
        SMALLER_SIDE,
        BIGGER_SIDE,
        THICKNESS,
        SIDE = "SMALLER_LEFT"
):
    #ENCONTRAR QUANTIDADE DE OBJETOS
    SMALLER_SIDE_AMOUNT_OF_OBJECTS = AMOUNT_OF_OBJECTS(SMALLER_SIDE)
    BIGGER_SIDE_AMOUNT_OF_OBJECTS = AMOUNT_OF_OBJECTS(BIGGER_SIDE)
    
    #FATOR DE DESLOCAMENTO
    BIGGER_OFFSET = OFFSET(BIGGER_SIDE, BIGGER_SIDE_AMOUNT_OF_OBJECTS)
    SMALLER_OFFSET = OFFSET(SMALLER_SIDE, SMALLER_SIDE_AMOUNT_OF_OBJECTS)
    
    #ENCONTRAR POSIÇÕES
    if SMALLER_SIDE_AXIS == X_AXIS:
        X_START = SMALLER_SIDE_START
    elif SMALLER_SIDE_AXIS == Y_AXIS:
        Y_START = SMALLER_SIDE_START
    elif SMALLER_SIDE_AXIS == Z_AXIS:
        Z_START = SMALLER_SIDE_START
        
    if BIGGER_SIDE_AXIS == X_AXIS:
        X_START = BIGGER_SIDE_START
    elif BIGGER_SIDE_AXIS == Y_AXIS:
        Y_START = BIGGER_SIDE_START
    elif BIGGER_SIDE_AXIS == Z_AXIS:
        Z_START = BIGGER_SIDE_START
        
    #FATORES DE ESCALONAMENTO
    SCALE_X = 1.0
    SCALE_Y = 1.0
    SCALE_Z = 1.0
    
    #FATORES DE DESLOCAMENTO
    ADD_X = 0.0
    ADD_Y = 0.0
    ADD_Z = 0.0
    
    #FATORES DE ROTAÇÃO
    ROTATION = math.radians(0)
        
    #ENCONTRAR ESPESSURA E FATORES DE ROTAÇÃO DO OBJETO        
    #CASO A ESPESSURA SEJA O EIXO X    
    if THICKNESS_SIDE_AXIS == X_AXIS:
        X_START = THICKNESS_START
        
            #MÉTODO PARA ESPESSURA NO EIXO X
        if "BIGGER" in SIDE:
            if BIGGER_SIDE_AXIS == Y_AXIS:
                #FATORES DE ROTAÇÃO
                ROTATION_AXIS = Z_AXIS
                ROTATION = math.radians(90)
                
                ADD_Y = BIGGER_OFFSET + STANDARD_OFFSET
                
                if "RIGHT" in SIDE:
                    #FATORES DE ESCALONAMENTO
                    SCALE_Z = -1.0
                    #FATORES DE DESLOCAMENTO
                    ADD_Z = SMALLER_SIDE
                    
            else:
                #FATORES DE ROTAÇÃO
                ROTATION_AXIS = Y_AXIS
                ROTATION = math.radians(-90)
                
                ADD_Z = BIGGER_OFFSET + STANDARD_OFFSET
                
                if "RIGHT" in SIDE:
                    #FATORES DE ESCALONAMENTO
                    SCALE_Y = -1.0
                    #FATORES DE DESLOCAMENTO
                    ADD_Y = SMALLER_SIDE
                    
        else: #"SMALLER" in SIDE:
            if BIGGER_SIDE_AXIS == Y_AXIS:
                
                ADD_Z = SMALLER_OFFSET + STANDARD_OFFSET
                
                #FATORES DE ROTAÇÃO
                ROTATION_AXIS = Y_AXIS
                ROTATION = math.radians(-90)
                
                if "RIGHT" in SIDE:
                    #FATORES DE ESCALONAMENTO
                    SCALE_Y = -1.0
                    #FATORES DE DESLOCAMENTO
                    ADD_Y = BIGGER_SIDE
            else:
                ADD_Y = SMALLER_OFFSET  + STANDARD_OFFSET
                
                #FATORES DE ROTAÇÃO
                ROTATION_AXIS = Z_AXIS
                ROTATION = math.radians(90)
                
                if "RIGHT" in SIDE:
                    #FATORES DE ESCALONAMENTO
                    SCALE_Z = -1.0
                    #FATORES DE DESLOCAMENTO
                    ADD_Z = BIGGER_SIDE
        
    #CASO A ESPESSURA SEJA O EIXO Y    
    elif THICKNESS_SIDE_AXIS == Y_AXIS:
        Y_START = THICKNESS_END
        
        ROTATION_AXIS = THICKNESS_SIDE_AXIS
        
        if "BIGGER" in SIDE:
            if BIGGER_SIDE_AXIS == X_AXIS:
                
                ADD_X = BIGGER_OFFSET + STANDARD_OFFSET
                
                if "RIGHT" in SIDE:
                    #FATORES DE DESLOCAMENTO
                    ADD_Z = SMALLER_SIDE
                    #FATORES DE ESCALONAMENTO
                    SCALE_Z = -1.0
            else:
                ADD_Z = BIGGER_OFFSET + STANDARD_OFFSET
                
                if "LEFT" in SIDE:
                    #FATORES DE ROTAÇÃO
                    ROTATION = math.radians(90)
                    #FATORES DE ESCALONAMENTO
                    SCALE_X = -1.0
                else: #"RIGHT" in SIDE:
                    #FATORES DE ROTAÇÃO
                    ROTATION = math.radians(-90)
                    #FATORES DE DESLOCAMENTO
                    ADD_X = SMALLER_SIDE

        else: #"SMALLER" in SIDE:
            if BIGGER_SIDE_AXIS == X_AXIS:
                
                ADD_Z = SMALLER_OFFSET + STANDARD_OFFSET
                
                #FATORES DE ROTAÇÃO
                ROTATION = math.radians(-90)
                
                if "LEFT"in SIDE:
                    #FATORES DE ESCALONAMENTO
                    SCALE_Z = -1.0
                else: #"RIGHT" in SIDE:
                    #FATORES DE DESLOCAMENTO
                    ADD_X = BIGGER_SIDE
            else:
                ADD_X = SMALLER_OFFSET + STANDARD_OFFSET
                
                if "RIGHT" in SIDE:
                    #FATORES DE ESCALONAMENTO
                    SCALE_Z = -1.0
                    #FATORES DE DESLOCAMENTO
                    ADD_Z = BIGGER_SIDE
                    
    #CASO A ESPESSURA SEJA O EIXO Z
    elif THICKNESS_SIDE_AXIS == Z_AXIS:
        Z_START = THICKNESS_START
        
        ROTATION_AXIS = THICKNESS_SIDE_AXIS
        
        SCALE_Z = -1.0
        
        if "BIGGER" in SIDE:
            if BIGGER_SIDE_AXIS == Y_AXIS:
                
                ADD_Y = BIGGER_OFFSET + STANDARD_OFFSET
                
                #FATORES DE ROTAÇÃO
                ROTATION = math.radians(90)
                
                if "LEFT" in SIDE:
                    #FATORES DE ESCALONAMENTO
                    SCALE_Y = -1.0
                else: #"RIGHT" in SIDE:
                    #FATORES DE DESLOCAMENTO
                    ADD_X = SMALLER_SIDE
            else:
                ADD_X = BIGGER_OFFSET + STANDARD_OFFSET
                
                if "RIGHT" in SIDE:
                    #FATORES DE DESLOCAMENTO
                    ADD_Y = SMALLER_SIDE
                    #FATORES DE ESCALONAMENTO
                    SCALE_Y = -1.0
                    
        else: #SMALLER in SIDE:
            if BIGGER_SIDE_AXIS == X_AXIS:
                
                ADD_Y = SMALLER_OFFSET + STANDARD_OFFSET
                
                #FATORES DE ROTAÇÃO
                ROTATION = math.radians(90)
                
                if "LEFT" in SIDE:
                    #FATORES DE ESCALONAMENTO
                    SCALE_Y = -1.0
                else: #"RIGHT" in SIDE:
                    #FATORES DE DESLOCAMENTO
                    ADD_X = BIGGER_SIDE
            else:
                ADD_X = SMALLER_OFFSET + STANDARD_OFFSET
                
                if "RIGHT" in SIDE:
                    #FATORES DE ESCALONAMENTO
                    SCALE_Y = -1.0
                    #FATORES DE DESLOCAMENTO
                    ADD_Y = BIGGER_SIDE
    
    #IMPORTAR OBJETOS
    IMPORTED_OBJECTS = IMPORT_OBJECTS(ACCESSORIES_PATH, IMPORTED_OBJECT_NAME)
    
    #POSIÇÃO  
    LOCATION_XYZ = (X_START + ADD_X, Y_START + ADD_Y, Z_START + ADD_Z)
    
    #ESCALA
    SCALE_XYZ = (SCALE_X, SCALE_Y, SCALE_Z)
    
    #QUANTIDADE
    if "BIGGER" in SIDE:
        AMOUNT = BIGGER_SIDE_AMOUNT_OF_OBJECTS
    else:
        AMOUNT = SMALLER_SIDE_AMOUNT_OF_OBJECTS


    CREATE_ARRAY_OBJECTS(IMPORTED_OBJECTS, LOCATION_XYZ, SCALE_XYZ, ROTATION_AXIS, ROTATION, AMOUNT, DISTANCE = STANDARD_DISTANCE)
    

################################### CÓDIGO PARA TESTES ###################################
if __name__ == "__main__":
    
    OBJECT_POSITIONS_DICT = RETURN_VERTICES_POSITIONING()
            
    APPEND_OBJECTS(
        OBJECT_POSITIONS_DICT["SMALLER_SIDE_AXIS"],
        OBJECT_POSITIONS_DICT["SMALLER_SIDE_START"],
        OBJECT_POSITIONS_DICT["SMALLER_SIDE_END"],
        OBJECT_POSITIONS_DICT["BIGGER_SIDE_AXIS"],
        OBJECT_POSITIONS_DICT["BIGGER_SIDE_START"],
        OBJECT_POSITIONS_DICT["BIGGER_SIDE_END"],
        OBJECT_POSITIONS_DICT["THICKNESS_SIDE_AXIS"],
        OBJECT_POSITIONS_DICT["THICKNESS_START"],
        OBJECT_POSITIONS_DICT["THICKNESS_END"],
        OBJECT_POSITIONS_DICT["SMALLER_SIDE"],
        OBJECT_POSITIONS_DICT["BIGGER_SIDE"],
        OBJECT_POSITIONS_DICT["THICKNESS"],
        "SMALLER_LEFT"
    )
            
    APPEND_OBJECTS(
        OBJECT_POSITIONS_DICT["SMALLER_SIDE_AXIS"],
        OBJECT_POSITIONS_DICT["SMALLER_SIDE_START"],
        OBJECT_POSITIONS_DICT["SMALLER_SIDE_END"],
        OBJECT_POSITIONS_DICT["BIGGER_SIDE_AXIS"],
        OBJECT_POSITIONS_DICT["BIGGER_SIDE_START"],
        OBJECT_POSITIONS_DICT["BIGGER_SIDE_END"],
        OBJECT_POSITIONS_DICT["THICKNESS_SIDE_AXIS"],
        OBJECT_POSITIONS_DICT["THICKNESS_START"],
        OBJECT_POSITIONS_DICT["THICKNESS_END"],
        OBJECT_POSITIONS_DICT["SMALLER_SIDE"],
        OBJECT_POSITIONS_DICT["BIGGER_SIDE"],
        OBJECT_POSITIONS_DICT["THICKNESS"],
        "SMALLER_RIGHT"
    )
            
    APPEND_OBJECTS(
        OBJECT_POSITIONS_DICT["SMALLER_SIDE_AXIS"],
        OBJECT_POSITIONS_DICT["SMALLER_SIDE_START"],
        OBJECT_POSITIONS_DICT["SMALLER_SIDE_END"],
        OBJECT_POSITIONS_DICT["BIGGER_SIDE_AXIS"],
        OBJECT_POSITIONS_DICT["BIGGER_SIDE_START"],
        OBJECT_POSITIONS_DICT["BIGGER_SIDE_END"],
        OBJECT_POSITIONS_DICT["THICKNESS_SIDE_AXIS"],
        OBJECT_POSITIONS_DICT["THICKNESS_START"],
        OBJECT_POSITIONS_DICT["THICKNESS_END"],
        OBJECT_POSITIONS_DICT["SMALLER_SIDE"],
        OBJECT_POSITIONS_DICT["BIGGER_SIDE"],
        OBJECT_POSITIONS_DICT["THICKNESS"],
        "BIGGER_LEFT"
    )        
            
    APPEND_OBJECTS(
        OBJECT_POSITIONS_DICT["SMALLER_SIDE_AXIS"],
        OBJECT_POSITIONS_DICT["SMALLER_SIDE_START"],
        OBJECT_POSITIONS_DICT["SMALLER_SIDE_END"],
        OBJECT_POSITIONS_DICT["BIGGER_SIDE_AXIS"],
        OBJECT_POSITIONS_DICT["BIGGER_SIDE_START"],
        OBJECT_POSITIONS_DICT["BIGGER_SIDE_END"],
        OBJECT_POSITIONS_DICT["THICKNESS_SIDE_AXIS"],
        OBJECT_POSITIONS_DICT["THICKNESS_START"],
        OBJECT_POSITIONS_DICT["THICKNESS_END"],
        OBJECT_POSITIONS_DICT["SMALLER_SIDE"],
        OBJECT_POSITIONS_DICT["BIGGER_SIDE"],
        OBJECT_POSITIONS_DICT["THICKNESS"],
        "BIGGER_RIGHT"
    )