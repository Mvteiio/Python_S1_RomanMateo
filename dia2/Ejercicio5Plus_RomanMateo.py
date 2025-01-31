## Ejercicio 5 Plus

def IMC(pesoKilogramos, estaturaMetros):
    IMC = 0
    IMC = pesoKilogramos/(estaturaMetros**2)
    IMCredondeado = round(IMC, 2)
    if IMC < 18.5:
        return f"Tu IMC es de {IMCredondeado}, por lo que tienes un peso bajo."
    elif IMC >= 18.5 and IMC <= 24.9:
        return f"Tu IMC es de {IMCredondeado}, por lo que tienes un peso normal."
    elif IMC >= 25 and IMC <= 29.9:
        return f"Tu IMC es de {IMCredondeado}, por lo que tienes Sobrepeso."
    elif IMC >= 30:
        return f"Tu IMC es de {IMCredondeado}, por lo que tienes obesidad."
    
pesoKilogramos = int (input("Dame tu peso en Kilogramos: "))
estaturaMetros = float (input("Dame tu estura en metros: "))

print(IMC(pesoKilogramos, estaturaMetros))

## Hecho por Mateo Roman Camargo // TI 1.044.624.790