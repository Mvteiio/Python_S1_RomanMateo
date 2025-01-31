## Ejercicio 4 del filtro en Python 

grande = int
peque = int
numero = int

grande = 0
peque = 0

for i in range (1,11):
    numero=int(input("Ingresa el numero: "))
    if grande == 0 or peque == 0:
        grande = numero
        peque = numero
    else:
        if numero > grande:
            grande = numero
        if numero < peque:
            peque = numero
print ("Grande: ", grande)
print ("Pequeño: ", peque)

    

## By Mateo Roman Camargo // TI 1044.624.790
