import json
from moduloPrecios import *

def abrirInmueblesJSON():
    with open("./inmuebles.json","r") as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarInmueblesJSON(dic):
    with open("./inmuebles.json","w") as outFile:
        json.dump(dic,outFile, indent=4, ensure_ascii=False)

dicInmuebles = {}
dicInmuebles = abrirInmueblesJSON()

print ("//////////////")
print ("//   MENU   //")
print ("//////////////")
print ("1. Crear inmueble. ")
print ("2. Ver propiedades segun presupuesto. ")
print ("3. Modificar una Propiedad.     ")
print ("4. Eliminar una propiedad. ")
eleccionUsuario = int(input("\nQue deseas hacer?: "))
match eleccionUsuario:
    case 1:
        inmuebleNuevo()
    case 2:
        asignarPrecios()
        verInmueblePresupuesto()
    case 3:
        modificarInmueble()
    case 4:
        eliminarPropiedad()



