import json

def abrirInmueblesJSON():
    with open("./inmuebles.json","r") as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarInmueblesJSON(dic):
    with open("./inmuebles.json","w") as outFile:
        json.dump(dic,outFile, indent=4, ensure_ascii=False)

dicInmuebles = {}
dicInmuebles = abrirInmueblesJSON()

def asignarPrecios ():
    for inmueble in dicInmuebles['inmuebles']:
        if inmueble['zona'] == "A":
            precio = (inmueble['metros']*1000)+(inmueble['habitaciones']*5000)
            if inmueble['garaje'] == True:
                precio = (precio + 15000)*(1-(2025-inmueble['year']) / 100)
                inmueble['precio']=precio
                guardarInmueblesJSON(dicInmuebles)

            else:
                precio = (precio)*(1-(2025-inmueble['year']) / 100)
                inmueble['precio']=precio
                guardarInmueblesJSON(dicInmuebles)
        elif inmueble['zona'] == "B":
            precio = (inmueble['metros']*1000)+(inmueble['habitaciones']*5000)
            if inmueble['garaje'] == True:
                precio = (precio + 15000)*(1-(2025-inmueble['year']) / 100)*1.5
                inmueble['precio']=precio
                guardarInmueblesJSON(dicInmuebles)

            else:
                precio = (precio)*(1-(2025-inmueble['year']) / 100)*1.5
                inmueble['precio']=precio
                guardarInmueblesJSON(dicInmuebles)

def inmuebleNuevo():
    nuevoYear = int(input("Ingresa el año en la que se creo el inmueble: "))
    nuevoMetros = int(input("Ingresa los metros que tiene esta propiedad: "))
    nuevoHabitaciones = int(input("Ingresa la cantidad de habitaciones de esta propiedad: "))
    nuevoGaraje = input("Tiene garaje? (S/N): ")
    garaje = nuevoGaraje == "S"
    nuevoZona = input("Es zona A o B?: ")

    numeroInmueble = len(dicInmuebles['inmuebles'])

    nuevoInmueble = {
        "numero": numeroInmueble + 1,
        "year": nuevoYear,
        "metros": nuevoMetros,
        "habitaciones": nuevoHabitaciones,
        "garaje": garaje,
        "zona": nuevoZona
    }

    dicInmuebles["inmuebles"].append(nuevoInmueble)
    print ("inmueble agregado con exito. ")
    guardarInmueblesJSON(dicInmuebles)

def verInmueblePresupuesto():
        presupuesto = int(input("Cual es tu presupuesto?: "))
        encontrado = False
        for inmueble in dicInmuebles['inmuebles']:
            if inmueble['precio'] <= presupuesto:
                print(f"Inmueble {inmueble['numero']} /  Antiguedad: {2025-inmueble['year']} años / Metros: {inmueble['metros']} / Habitaciones: {inmueble['habitaciones']} / Garaje: {inmueble['garaje']} / Zona: {inmueble['zona']} / Precio: ${inmueble['precio']}")
                encontrado = True
        if not encontrado:
            print("No hay propiedades por este precio :(")

def modificarInmueble():
    numeroBuscar = int(input("Ingresa el numero de la propiedad que deseas modificar: "))
    for inmueble in dicInmuebles['inmuebles']:
        if inmueble['numero']==numeroBuscar:

            nuevoYear = int(input("Ingresa el año en la que se creo el inmueble: "))
            nuevoMetros = int(input("Ingresa los metros que tiene esta propiedad: "))
            nuevoHabitaciones = int(input("Ingresa la cantidad de habitaciones de esta propiedad: "))
            nuevoGaraje = input("Tiene garaje? (S/N): ")
            garaje = nuevoGaraje == "S"
            nuevoZona = input("Es zona A o B?: ")

            numeroInmueble = len(dicInmuebles['inmuebles'])

            nuevoInmueble = {
                "numero": numeroBuscar,
                "year": nuevoYear,
                "metros": nuevoMetros,
                "habitaciones": nuevoHabitaciones,
                "garaje": garaje,
                "zona": nuevoZona
            }

            dicInmuebles["inmuebles"][numeroBuscar-1]=(nuevoInmueble)
            print ("inmueble modificado con exito. ")
            guardarInmueblesJSON(dicInmuebles)

def eliminarPropiedad():
    numeroEliminar = int(input("Ingresa el numero de la propiedad que deseas eliminar: "))

    for inmueble in dicInmuebles['inmuebles']:
        if inmueble['numero'] == numeroEliminar:
            dicInmuebles['inmuebles'].pop(numeroEliminar-1)
            print("Inmueble eliminado con exito. ")
            guardarInmueblesJSON(dicInmuebles)