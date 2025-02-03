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


nombreApellido=int(input("Deseas cambiar el nombre o el apellido de un estudiante?(1/2): "))

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
        case _:
            print ("Solo puedes elegir uno de los dos numero anteriores")
    salirConfirmacion = int(input("Deseas salir del menu o seguir editando la lista?(1/2): "))
    if salirConfirmacion == 1:
        break
    elif salirConfirmacion == 2:
        nombreApellido=int(input("Deseas cambiar el nombre o el apellido de un estudiante?(1/2): "))
    

       
    
    






