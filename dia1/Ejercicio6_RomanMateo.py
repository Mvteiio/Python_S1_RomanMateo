## Ejercicio 6 del filtro en Python 

N = int(input("Ingrese el numero de empleados: "))
totalBruto = 0
totalEps = 0
totalPension = 0
totalNeto = 0
pension = 0

mayorSueldo = 0
menorSueldo = 99999999



for i in range (1, N+1):

    nombre = input("Ingrese el nombre del empleado: ")
    horas = int(input("Ingrese las horas trabajadas: "))
    bruto = horas * 20000
    eps = bruto * 0.04
    pension = bruto * 0.04
    neto = bruto - eps - pension

    totalBruto = totalBruto + bruto
    totalEps = totalEps + eps
    totalPension = totalPension + pension
    totalNeto = totalNeto + neto

    
    
    if neto > mayorSueldo:
        mayorSueldo = neto
        nombreMayor = nombre
    if neto < menorSueldo:
        menorSueldo = neto
        nombreMenor = nombre
    print("Empleado ", nombre)
    print("Sueldo bruto: ", bruto)
    print("EPS: ", eps)
    print("Pension: ", pension)
    print("Sueldo neto: $", neto)

promedioBruto = totalBruto/N
promedioNeto = totalNeto/N

print("Totales: ")
print("Total salarios brutos: $", totalBruto)
print("Total EPS: $", totalEps)
print("Total Pension: $", totalPension)
print("Total salarios netos: $", totalNeto)
print("Empleado que más gana: ", nombreMayor)
print("Sueldo del empleado que mas gana: $", mayorSueldo)
print("Empleado que menos gana: ", nombreMenor)
print("Promedio salarios brutos: ", promedioBruto)
print("Promedio salarios netos: $", promedioNeto)

## By Mateo Roman Camargo // TI 1044.624.790