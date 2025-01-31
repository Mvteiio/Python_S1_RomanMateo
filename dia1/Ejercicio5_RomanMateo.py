## Ejercicio 5 del filtro en Python 

termino1 = 1
termino2 = 1
termino3 = 0
termino4 = 0

print(termino1)
print(termino2)

for i in range (3, 6):
    termino3 = termino1+termino2
    print (termino3)
    termino4 = termino2-termino3
    print (termino4)
    termino1 = termino3
    termino2 = termino4


## By Mateo Roman Camargo // TI 1044.624.790