from ejercicioListas_RomanMateo import cambioNombre, cambioApellido, agregarEstudiante, borrarEstudiante

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


salirConfirmacion = True

while salirConfirmacion == True:
    print("          ////// MENU //////")
    print("1. Cambiar nombre de un estudiante.")
    print("2. Cambiar los apellidos de un estudiante.")
    print("3. Agregar un estudiante a la lista.")
    print("4. Eliminar un estudiante de la lista.")
    nombreApellido = int(input("¿Qué deseas hacer?: "))
    match nombreApellido:
        case 1:
            print(cambioNombre()) 
        case 2:
            print(cambioApellido())
        case 3:
            print(agregarEstudiante())
        case 4:
            print(borrarEstudiante())
        case _:
            print ("Solo puedes elegir una de las 4 opciones.")
    salirConfirmacion = int(input("Deseas salir del menu o seguir editando la lista?(1/2): "))
    if salirConfirmacion == 1:
        print("Vuelve pronto :)")
        salirConfirmacion = False
    elif salirConfirmacion == 2:
        print("Seguiremos editando la lista")
        salirConfirmacion = True
    else:
        print("Opcion no valida, siguiendo con el menu")
        salirConfirmacion = True
 