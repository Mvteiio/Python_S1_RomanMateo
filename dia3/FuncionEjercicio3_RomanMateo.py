import math

def numerosPrimos (numero):
    if numero % 2 == 0:
        return "Este numero es par"
    else:
        return "Este numero es impar"
    print ("") 

def primoCompuesto (numeroPrimoCompuesto):
    primo = 0
    compuesto = 0
    for i in range (1, numeroPrimoCompuesto+1):
        if (numeroPrimoCompuesto%i == 0):
            primo = primo + 1
            compuesto = compuesto + 1
    if primo == 2:
        return "Este numero es primo."
    elif compuesto > 2:
        return "Este numero es compuesto"
    
def cuadradoPerfecto (numeroCuadrado):
    raiz = math.sqrt(numeroCuadrado)
    return raiz.is_integer()



          

numero = int(input("Que numero deseas conocer si es par o impar?: "))
print(numerosPrimos(numero))  

numeroPrimoCompuesto= int(input("Que numero deseas conocer si es primo o compuesto: "))
print(primoCompuesto (numeroPrimoCompuesto))

numeroCuadrado = int(input("Que numero deseas saber si es un cuadrado perfecto?: "))
if (cuadradoPerfecto(numeroCuadrado)):
    raiz = math.sqrt(numeroCuadrado)
    print (f"{numeroCuadrado} SI es un cuadrado perfecto, es el cuadrado de {raiz}")
else:
    print (f"{numeroCuadrado} NO es un cuadrado perfecto")