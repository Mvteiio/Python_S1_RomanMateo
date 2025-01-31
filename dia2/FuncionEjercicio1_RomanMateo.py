
def celciusToFahrenheit (gradosCelsius):
    gradosFahrenheit = 0
    gradosFahrenheit = ((gradosCelsius*9)/5)+32
    return gradosFahrenheit

def fahrenheitToCelsius (gradosFahrenheit):
    gradosCelsius = 0
    gradosCelsius = (gradosFahrenheit-32)/1.8
    return gradosCelsius

while True:
    try:
        celsiusFahrenheit = int(input("Deseas pasar de grados Celsius a Fahrenheit o viceversa? (1/2) "))
        if celsiusFahrenheit in [1, 2]:
            break  # Sale del bucle si la entrada es válida
        else:
            print("Por favor, ingresa 1 para convertir a Fahrenheit o 2 para convertir a Celsius.")
    except ValueError:
        print("Error: Solo puedes escribir números. Inténtalo de nuevo.")

if celsiusFahrenheit == 1:
    gradosCelsius = int(input("Dame los grados Celsius que quiere convertir a Fahrenheit: "))
    print ("Esto son ",celciusToFahrenheit(gradosCelsius), " grados Fahrenheit")

if celsiusFahrenheit == 2:
    gradosFahrenheit = int(input("Dame los grados Fahrenheit que quiere convertir a Celsius: "))
    print ("Esto son ",fahrenheitToCelsius(gradosFahrenheit), " grados Celsius")