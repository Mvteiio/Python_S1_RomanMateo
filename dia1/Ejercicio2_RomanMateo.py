## Ejercicio 2 del filtro en Python 

cantidadTerminos = int(input("Cual termino deseas ver? "))
print("La cantidad de términos es: ", cantidadTerminos)
if cantidadTerminos <= 0:
    print(0)
sumatoria = 0

for i in range (1, cantidadTerminos):
    if (i % 2 == 0):
        sumatoria = sumatoria - (1/i)
    else:
        sumatoria = sumatoria + (1/i)

print ("La sumatoria dio: ", sumatoria)

## By Mateo Roman Camargo // TI 1044.624.790