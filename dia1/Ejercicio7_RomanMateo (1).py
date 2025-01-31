## Ejercicio 7 del filtro en Python 

num1 = int(input("Ingresa numero 1: "))
num2 = int(input("Ingresa numero 2: "))

suma1 = 0
suma2 = 0

for i in range (1, num1):
    if (num1 % i == 0):
        suma1 = suma1 + i
for i in range (1, num2):
    if (num2 % i == 0):
        suma2 = suma2 + i
if suma1 == num2 and suma2 == num1:
    print("Son bros los numeros ", num1, "y ", num2)
else:
    print("No son bros los numeros ", num1, "y ", num2)
           



## By Mateo Roman Camargo // TI 1044.624.790