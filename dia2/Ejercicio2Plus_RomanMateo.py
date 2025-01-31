## Ejercicio 2 Plus 

def conversorUnidades (elegirConversion):
    match elegirConversion:
        case 1:
            kilometros = int(input("Cuanto kilometros deseas convertir a millas?: "))
            if kilometros > 0:
                millas = 0
                millas = kilometros*0.621371
                return f"Esto son {millas} millas"
            else:
                return f"No puedo hacer esta operacion con numeros negativos o 0"
        case 2:
            celsius = int(input("Que temperatura en celsius deseas convertir a fahrenheit?: "))
            if celsius > 0:
                fahrenheit = 0
                fahrenheit = (celsius*1.8)+32
                return f"Esto son {fahrenheit} grados fahrenheit"
            else:
                return f"No puedo hacer esta operacion con numeros negativos o 0"
        case 3: 
            kilogramos = int(input("Cuantos kilogramos deseas pasar a libras?: "))
            if kilogramos > 0:
                libras = 0
                libras = kilogramos*2.2046
                return f"Esto son {libras} libras"
            else:
                return f"No puedo hacer esta operacion con numeros negativos o 0"
        case _: 
            return f"Debes elegir una de las 3 opciones"
            


print("Que quieres hacer?")
print("1. Pasar de kilometros a millas ")
print("2. Pasar de celsius a fahrenheit ")
print("3. Pasar de kilogramos a libras")
elegirConversion = int(input("Elige una opcion: "))
print(conversorUnidades(elegirConversion))

## Hecho por Mateo Roman Camargo // TI 1.044.624.790