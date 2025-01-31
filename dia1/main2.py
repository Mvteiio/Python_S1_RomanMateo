## ////////////////////////
## -- FUNDAMENTOS DE PROGRAMACIÓN
## ////////////////////////
print("Hola Mundo!!!!!!")

## -- TIPOS DE DATOS --
##1. String ""
cadenaTexto = "Textico"
print(type(cadenaTexto)) ##Imprimir el tipo de dato

##2. Numero Entero - int
numeroEntero = 2
print(type(numeroEntero))

##3. Numero flotante - float
numeroFlotante= 1.1
print(type(numeroFlotante))

##4. Numero Doble - double
numeroDouble = 3.1416586945930949587349567
print(type(numeroDouble))

##5. Booleano - True/False
booleanito = True
print(type(booleanito))


##Entradas por parte del usuario
x=input("Ingresa un número:") ## Todo input es texto - String
print(type(x))


##Conversion de tipos de datos - casteo
## Sintáxis - tipoDato(Dato_a_convertir)
x=int(input("Ingresa un número:"))
print(type(x))

##Ejercicio - sumar dos numeros por parte del usuario
num1 = int(input("Ingresa el primer número:"))
num2 = int(input("Ingresa el segundo número:"))
resultadoSumatoria= num1+num2
print("El resultado dado es de:", resultadoSumatoria)

##Ciclos for y while 
##Ciclo for nomal
for i in range(5):##i será el iterador e irá hasta el 5
    print(i)
##Ciclo desde hasta
print("#############")
for i in range(0,5):##i será el iterador e irá desde el cero hasta el 5
    print(i)
##Ciclo con pasos
print("#############")
for i in range(0,5,2):##i será el iterador e irá desde el cero hasta el 5 en paso de 2 en 2
    print(i)

##Ciclo While
booleanito1 = True
while (booleanito1 == True):
    print(booleanito1)
    booleanito1 = False

##4 tipos de funciones
##Funcion sin parametros y sin retorno
def funcion1():
    print("Soy una funcion increible!!!!!!!")


funcion1()

##Funcion sin parametros pero con retorno
def funcion2():
    return 5
print("Su número es:",funcion2())

##Funcion con parámetros pero sin retorno
def funcion3 (nombre,apellido):
    print("Su nombre es:",nombre," ",apellido)
funcion3("Edgar","Acevedo")

##Función con parámetros y retorno
def funcion4(a,b):
    c= a**b
    return c

funcionA= int(input("Ingrese el numero base:"))
funcionB=int(input("Ingrese la elevación deseada:"))
print("El resultado de su elevación es de:",funcion4(funcionA,funcionB))
##Desarrollado por : Pedro Gomez / C.C:1.666.555.444