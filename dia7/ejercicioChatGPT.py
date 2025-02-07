import json

def abrirJSON():
    dicFinal={}
    with open("./ejercicioChatGPT.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./ejercicioChatGPT.json",'w') as outFile:
        json.dump(dic,outFile)

# CRUD 1. crear 2. leer. 3. actualizar. 4. borrar
infoLibross={}
infoLibross=abrirJSON()

def mostrarLibros ():
    for i in range (len(infoLibross["infoLibros"])):
        print("\nLibro: ", i+1)
        print("Titulo:", infoLibross["infoLibros"][i]["Titulo"])
        print("Genero:", infoLibross["infoLibros"][i]["Genero"])
        print("Autor:", infoLibross["infoLibros"][i]["Autor"])
        print("Publicacion:", infoLibross["infoLibros"][i]["Publicacion"])
    return ""

def mostrarUsuario():
    for i in range(len(infoLibross["infoUsuario"])):
        print("\nUsuario: ", i+1)
        print("Identificador:", infoLibross["infoUsuario"][i]["Identificador"])
        print("Nombre del usuario:", infoLibross["infoUsuario"][i]["nombreUsuario"])
        print("Tipo de usuario:", infoLibross["infoUsuario"][i]["tipoUsuario"])
    return ""

while True:
    print("///////////////")
    print("///   MENU  ///")
    print("///////////////")
    print("1. Agregar un libro o usuario.")
    print("2. Mostrar la lista de libros/usuarios.")
    print("3. Cambiar un libro/usuario.")
    print("4. Borrar un libro/usuario. ")
    print("5. Salir del menu.")
    opcion1 = int(input("Elige que harás: "))

    if opcion1 == 1:
        libroUsuario = int(input("Deseas agregar un Libro o un Usuario?(1/2): "))
        if libroUsuario == 1:
            tituloNuevo = input("Indica el titulo del libro a agregar: ")
            generoNuevo = input("Indica el genero del libro a agregar: " )
            autorNuevo = input("Indica el autor del libro a agregar: ")
            publicacionNuevo = input("Indica la fecha de publicacion del libro: ")
            
            nuevoLibro = {
                "Titulo": tituloNuevo,
                "Genero": generoNuevo,
                "Autor": autorNuevo,
                "Publicacion": publicacionNuevo
            }

            infoLibross["infoLibros"].append(nuevoLibro)
            guardarJSON(infoLibross)
            print("Libro agregado exitosamente")
        elif libroUsuario == 2:
            identificadorNuevo = input("Escribe el identificador del usuario ")
            nombreNuevo = input("Indica el nombre del usuario: ")
            tipoUsuarioNuevo = input("Indica el tipo de usuario: ")

            nuevoUsuario = {
                "Identificador": identificadorNuevo,
                "nombreUsuario": nombreNuevo,
                "tipoUsuario": tipoUsuarioNuevo
            }

            infoLibross["infoUsuario"].append(nuevoUsuario)
            guardarJSON(infoLibross)
            print("Usuario agregado exitosamente")

    elif opcion1 == 2:
        mostrarLibroUsuario = int(input("Quieres ver la lista de Libros o de Usuarios?(1/2): "))
        if mostrarLibroUsuario == 1:
            print(mostrarLibros())
        elif mostrarLibroUsuario == 2:
            print(mostrarUsuario())
        else:
            print("Solo puedes elegir una de las dos opciones. ")

    elif opcion1 == 3:
        cambiarLibroUsuario = int(input("Quieres modificar un Libro o un Usuario?(1/2): "))
        if cambiarLibroUsuario == 1:
            print(mostrarLibros())
            eleccionCambio = int(input("Cual libro deseas modificar?: "))
            cambioTitulo = input("Escribe el nuevo titulo del libro: ")
            cambioGenero = input("Escribe el nuevo genero del libro: ")
            cambioAutor = input("Escribe el nuevo autor del libro: ")
            cambioPublicacion = input("Escribe la nueva fecha de publicacion del libro: ")

            cambioLibro = {
                "Titulo": cambioTitulo,
                "Genero": cambioGenero,
                "Autor": cambioAutor,
                "Publicacion": cambioPublicacion
            }
        
            infoLibross['infoLibros'][eleccionCambio - 1] = cambioLibro
            guardarJSON(infoLibross)
            print("Libro modificado exitosamente")

        elif cambiarLibroUsuario == 2:
            print(mostrarUsuario())
            eleccionCambio = int(input("\nCual usuario deseas modificar?: "))
            cambioIdentificador = input("Escribe el nuevo identificador del usuario: ")
            cambioUsuario = input("Escribe el nuevo usuario: ")
            cambioTipo = input("Escribe el nuevo tipo de usuario: ")

            cambioUsuario = {
                "Identificado": cambioIdentificador,
                "nombreUsuario": cambioUsuario,
                "tipoUsuario": cambioTipo,
            }
        
            infoLibross['infoUsuario'][eleccionCambio - 1] = cambioUsuario 
            guardarJSON(infoLibross)
            print("Usuario modificado exitosamente")
    elif opcion1 == 4:
        borrarLibroUsuario = int(input("Quieres borrar un libro o un usuario?(1/2): "))
        if borrarLibroUsuario == 1:
            print (mostrarLibros())
            borrarEleccion = int(input("\nCual libro deseas borrar?: "))
            infoLibross["infoLibros"].pop(borrarEleccion-1)
            guardarJSON(infoLibross)
            print("Libro eliminado con exito. ")
        
        if borrarLibroUsuario == 2:
            print (mostrarUsuario())
            borrarEleccion = int(input("\nCual usuario deseas borrar?: "))
            infoLibross["infoUsuario"].pop(borrarEleccion-1)
            guardarJSON(infoLibross)
            print("Usuario eliminado con exito. ")
    elif opcion1 == 5:
        print("\nSaliendo del programa :)")
        break









