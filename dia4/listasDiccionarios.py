##Listas 
## Una lista es una estructura de datos que organiza y 
# almacena elementos de manera secuencial y ordenada


##nombre = ["Pedro","Edgar","David"]
## Carateristicas:
# 1. El tamaño de una lista es dinámico, pues se pueden ingresar x
## datos.

nombres=["Pedro","David","Edgar"]
print(len(nombres))
nombres.append("Aguilar") ## Agregar un elemento en cola ["Pedro","David","Edgar","Aguilar"]
print(len(nombres))
## 2. Para recorrer una lista se utilizan los índices, los cuales
## son la posición adentro de la lista.
print(nombres[-1])
## 3. En Python, las listas pueden almacenar diferentes tipos de datoa a la vez
nombres.append(True)
print(nombres)

##Funciones mas comunes 
#Agregar: append() para agregar en Cola
listaNueva=[]
listaNueva.append("Cajasan")
print(listaNueva)

##Extender: Permite agregar una lista adicional a una lista existente
lista1=[1,2,3,4,5]
lista1.extend([6,7,8,9,0])
print(lista1)

##Insertar en un índice: Permite agregar un elemento en una posición exacta
listaIndice= ["rojo","azul"]
listaIndice.insert(1,"amarillo")## ["rojo",,"azul"] --> ["rojo","amarillo","azul"]
print(listaIndice)

##Reemplazar un ítem en un indice : Permite reemplazar un ítem que está en un índice en específico
listaReemplazar = ["Pedro","Gomez"]
listaReemplazar[1]="Bonilla"
print(listaReemplazar)

##Eliminar el último ítem en cola: Para eliminar el último ítem en cola utilizamos pop() solo , 
# sino le ingresamos el índice y este lo eliminará
listaPop=["Andres","Camargo","David","Pérez"]
listaPop.pop()
print(listaPop)
listaPop.pop(0)
print(listaPop)

##Contar elementos: Para contar cuantos elementos iguales hay en una lista utilizamos .count()
vocales = ["a", "e", "i", "o", "u", "a"]
apariciones = vocales.count("a") ##Retornar el número de las veces que la "a" esta presente en la lista
print(apariciones)

##Ordenamiento

ListaOrdenada = [1, 6, 4, 5, 2, 9, 0]
ListaOrdenada.sort()
print(ListaOrdenada)

estudiantes = [
    "Adrián Quintero Pinzón",
    "Alejandra Pinzón Alvarez",
    "Ámbar Isabella Plata López",
    "Andrés David Reyes Espinel",
    "Aura Camila Pico Araque",
    "Camilo Andrés Suárez Fuentes",
    "Daniel Esteban Guerrero Quintero",
    "David Santiago Vera Mendez",
    "Edgar Leonardo Acevedo Arteaga",
    "Gerson Steven Chaparro Martínez",
    "Harley Yefrey Cabrales Vargas",
    "John Stiven Negron Regalado",
    "Juan David Saavedra Jaimez",
    "Juan David Santoyo Jaimes",
    "Juan David Vargas Soto",
    "Juan Eduardo Pinilla Guzmán",
    "Juan Fernando Umaña Barragan",
    "Juan Jose Abril Roman",
    "Maria Juliana Saavedra Mejia",
    "Mateo Roman Camargo",
    "Naya Zarela Lizcano Jaimes",
    "Nicolas Chedraui Mantilla",
    "Omar Fernando Granados Parra",
    "Santiago Aguilar Vesga",
    "Santiago Andrés Quiñonez Sosa",
    "Santiago Jaimes Perez",
    "Sara Sofía Díaz Rodríguez",
    "Sayara Yurley Aparicio Arciniegas",
    "Sergio Andrés Rueda Hernández",
    "Simón Dante Salamanca Galvis",
    "Thomas Sebastián Bastos Garcia",
    "Vladimir Diaz Contreras"
]

for i in range (len(estudiantes)):
    print (estudiantes[i])
