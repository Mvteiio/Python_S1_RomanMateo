## Ejercicio 4 Plus

def conversorMoneda (opcionConvertir):
    match opcionConvertir:
        case 1:
            cantidadDolares = int(input("Cuantos dolares deseas pasar a Euros?: "))
            euros = 0
            euros = cantidadDolares * 0.85
            return f"${cantidadDolares} Dolares son ${euros} Euros."
        case 2: 
            cantidadDolares = int(input("Cuantos dolares deseas pasar a COP?: "))
            COP = 0
            COP = cantidadDolares * 4100
            return f"${cantidadDolares} Dolares son ${COP} Pesos colombianos."
        case 3:
            cantidadDolares = int(input("Cuantos dolares deseas pasar a Yenes?: "))
            yenes = 0
            yenes = cantidadDolares * 110
            return f"${cantidadDolares} Dolares son ${yenes} Yenes."
        case _:
            return f"Debes elegir una de las 3 opciones de conversion."
        
print("Que quieres hacer?")
print("1. Convertir Dolares a Euros")
print("2. Convertir Dolares a Pesos Colombianos ")
print("3. Convertir Dolares a Yenes")
opcionConvertir = int(input("Elige una opcion: "))
print(conversorMoneda(opcionConvertir))

## Hecho por Mateo Roman Camargo // TI 1.044.624.790