#Cargamos las librerias necesarias
import bpy
import random

#Funcion para crear a un personaje aleatorio
def crearPersona(altura=1.70, posicion=(0,0,0), cont=0):
    """ Se crea una sola persona en una determinada altura y posicion"""
    
    pathgeneral = bpy.path.abspath("//")    #Cogemos la ruta hacia este blend
    
    #CUERPO
    #Importamos cuerpo principal le damos nombre y lo colocamos
    path = pathgeneral + "Body_1.blend/Object/"
    archivo = "Body"
    bpy.ops.wm.append(filename=archivo, directory=path)
    person = "persona_"+str(cont)
    bpy.data.objects["Body"].name = person
    
    #ROPA
    #Importamos un vestido
    v = str(random.randint(1, 3))  #Cogemos uno de los vestidos al azar
    #path = "C:/Users/gabri/Desktop/peoplecreator/vestido_"+v+".blend/Object/"
    path = pathgeneral + "vestido_"+v+".blend/Object/"
    archivo = "Dress"
    bpy.ops.wm.append(filename=archivo, directory=path)
    #Hacemos que el vestido se emparente al cuerpo
    vestido = "vestido_"+str(cont)
    bpy.data.objects["Dress"].name = vestido
    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects[vestido].select = True
    bpy.context.scene.objects.active = bpy.data.objects[person]
    bpy.ops.object.parent_set(keep_transform=True)
    
    #PELO
    #Importamos pelo
    p = str(random.randint(1, 3))  #Cogemos uno de los peinados al azar
    path = pathgeneral + "hair_"+p+".blend/Object/"
    archivo = "Hair"
    bpy.ops.wm.append(filename=archivo, directory=path)
    #Hacemos que el pelo se emparente al cuerpo
    hair = "hair_"+str(cont)
    bpy.data.objects["Hair"].name = hair
    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects[hair].select = True
    bpy.context.scene.objects.active = bpy.data.objects[person]
    bpy.ops.object.parent_set(keep_transform=True)
    
    #ALTURA
    bpy.data.objects[person].dimensions[1] = altura
    
    #POSICION
    bpy.data.objects[person].location = posicion


def crearVariasPersonas(nper):
    """ Crea varias personas"""
    
    for n in range(1,nper+1):
        altura = random.random()*(2-1.50)+1.50
        xale = random.randrange(-10,10)
        yale = random.randrange(-10,10)
        posicion = (xale, yale, 0)
        crearPersona(altura, posicion, n)

crearVariasPersonas(9)
