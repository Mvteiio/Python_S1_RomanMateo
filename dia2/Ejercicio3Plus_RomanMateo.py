## Ejercicio 3 Plus

def clasificacionYear (año):
    if año % 4 == 0 or año % 400 == 0:
        return f"Este año es bisiesto"
    else:
        return "Este año es comun, no es bisiesto"
    
año = int(input("Que año deseas saber si es bisiesto o comun?: "))
print (clasificacionYear(año))

## Hecho por Mateo Roman Camargo // TI 1.044.624.790