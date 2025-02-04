nombres = [
    ["Adrián"],
    ["Alejandra"],
    ["Ámbar", "Isabella"],
    ["Andrés", "David"],
    ["Aura", "Camila"],
    ["Camilo", "Andrés"],
    ["Daniel", "Esteban"],
    ["David", "Santiago"],
    ["Edgar", "Leonardo"],
    ["Gerson", "Steven"],
    ["Harley", "Yefrey"],
    ["John", "Stiven"],
    ["Juan", "David"],
    ["Juan", "David"],
    ["Juan", "David"],
    ["Juan", "Eduardo"],
    ["Juan", "Fernando"],
    ["Juan", "Jose"],
    ["Maria", "Juliana"],
    ["Mateo", "Roman"],
    ["Naya", "Zarela"],
    ["Nicolas"],
    ["Omar", "Fernando"],
    ["Santiago"],
    ["Santiago", "Andrés"],
    ["Santiago"],
    ["Sara", "Sofía"],
    ["Sayara", "Yurley"],
    ["Sergio", "Andrés"],
    ["Simón", "Dante"],
    ["Thomas", "Sebastián"],
    ["Vladimir"]
]

apellidos = [
    ["Quintero", "Pinzón"],
    ["Pinzón", "Alvarez"],
    ["Plata", "López"],
    ["Reyes", "Espinel"],
    ["Pico", "Araque"],
    ["Suárez", "Fuentes"],
    ["Guerrero", "Quintero"],
    ["Vera", "Mendez"],
    ["Acevedo", "Arteaga"],
    ["Chaparro", "Martínez"],
    ["Cabrales", "Vargas"],
    ["Negron", "Regalado"],
    ["Saavedra", "Jaimez"],
    ["Santoyo", "Jaimes"],
    ["Vargas", "Soto"],
    ["Pinilla", "Guzmán"],
    ["Umaña", "Barragan"],
    ["Abril", "Roman"],
    ["Saavedra", "Mejia"],
    ["Camargo"],
    ["Lizcano", "Jaimes"],
    ["Chedraui", "Mantilla"],
    ["Granados", "Parra"],
    ["Aguilar", "Vesga"],
    ["Quiñonez", "Sosa"],
    ["Jaimes", "Perez"],
    ["Díaz", "Rodríguez"],
    ["Aparicio", "Arciniegas"],
    ["Rueda", "Hernández"],
    ["Salamanca", "Galvis"],
    ["Bastos", "Garcia"],
    ["Diaz", "Contreras"]
]

print("          ////// MENU //////")
print("1. Cambiar nombre de un estudiante.")
print("2. Cambiar los apellidos de un estudiante.")
print("3. Agregar un estudiante a la lista.")
print("4. Eliminar un estudiante de la lista.")
nombreApellido=int(input("Qué deseas hacer?: "))

while True:
    match nombreApellido:
        case 1:
            for i in range (len(nombres)):
                nombreCompleto = " ".join(nombres[i]) + " " + " ".join(apellidos[i])
                print(f"{i + 1}. {nombreCompleto}")
            nombreNumero = int(input("Cual es el numero del estudiante que deseas cambiarle el nombre?: "))
            nombreNuevo =input("Cual es el nombre al que deseas cambiar?: ")
            nombres[nombreNumero-1]= [nombreNuevo]
            for i in range (len(nombres)):
                nombreCompleto = " ".join(nombres[i]) + " " + " ".join(apellidos[i])
                print(f"{i + 1}. {nombreCompleto}")
        case 2:
            for i in range (len(nombres)):
                nombreCompleto = " ".join(nombres[i]) + " " + " ".join(apellidos[i])
                print(f"{i + 1}. {nombreCompleto}")
            apellidoNumero = int(input("Cual es el numero del estudiante que deseas cambiarle el apellido?: "))
            apellidoNuevo =input("Cual es el apellido al que deseas cambiar (escriba los dos apellidos)?: ")
            apellidos[apellidoNumero-1]= [apellidoNuevo]
            for i in range (len(nombres)):
                nombreCompleto = " ".join(nombres[i]) + " " + " ".join(apellidos[i])
                print(f"{i + 1}. {nombreCompleto}")
        case 3:
            nuevoNombre = input("Escribe el nombre del estudiante que deseas agregar: ")
            nombres.append([nuevoNombre])
            nuevoApellido = input("Escribe los apellidos del usuario que deseas agregar: ")
            apellidos.append([nuevoApellido])
            for i in range (len(nombres)):
                nombreCompleto = " ".join(nombres[i]) + " " + " ".join(apellidos[i])
                print(f"{i + 1}. {nombreCompleto}")
        case 4:
            for i in range (len(nombres)):
                nombreCompleto = " ".join(nombres[i]) + " " + " ".join(apellidos[i])
                print(f"{i + 1}. {nombreCompleto}")
            estudianteBorrar = int(input("Escribe el número del estudiante a borrar: "))
            nombres.pop(estudianteBorrar-1)
            apellidos.pop(estudianteBorrar-1)
            for i in range (len(nombres)):
                nombreCompleto = " ".join(nombres[i]) + " " + " ".join(apellidos[i])
                print(f"{i + 1}. {nombreCompleto}")

        case _:
            print ("Solo puedes elegir uno de los dos numero anteriores")

    salirConfirmacion = int(input("Deseas salir del menu o seguir editando la lista?(1/2): "))
    if salirConfirmacion == 1:
        print("Vuelve pronto :)")
        break
    elif salirConfirmacion == 2:
        print("          ////// MENU //////")
        print("1. Cambiar nombre de un estudiante.")
        print("2. Cambiar los apellidos de un estudiante.")
        print("3. Agregar un estudiante a la lista.")
        print("4. Eliminar un estudiante de la lista.")
        nombreApellido=int(input("Qué deseas hacer?: "))
    

       
    
    






