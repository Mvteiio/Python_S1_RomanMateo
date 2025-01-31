## Ejercicio 1 Plus 

def sistemaRecomendaciones (clima, horaDia):
    match clima:
        case "soleado":
            if horaDia == "mañana":
                return ("Toma un refresco bien frio")
            elif horaDia == "tarde":
                return ("Come algo que te de energia para este solazo")
            elif horaDia == "noche":
                return  ("Una parrillade de verduras")    
            else:
                return ("No te puedo ayudar si no es un momento del dia de los que te dije")
        case "lluvioso":
            if horaDia == "mañana":
                return ("Toma un cafecito caliente")
            elif horaDia == "tarde":
                return ("Come un almuerzo calentico para esta lluvia")
            elif horaDia == "noche":
                return ("Para esta noche lluviosa nada mejor que un chocolate")    
            else:
                return ("No te puedo ayudar si no es un momento del dia de los que te dije")
        case "frio":
            if horaDia == "mañana":
                return ("Toma un chocolate con pan")
            elif horaDia == "tarde":
                return ("Un estofado de carne caeria de lujo")
            elif horaDia == "noche":
                return ("Unas pastas estilo italiano serian perfectas")    
            else:
                return ("No te puedo ayudar si no es un momento del dia de los que te dije")
        case _:
            print ("Solo te puedo ayudar con los 3 climas que te dije. ")

clima = input("Qué clima está haciendo en tu zona?(soleado, lluvioso, frio): " )
horaDia = input("Qué momento del dia es?(mañana, tarde, noche): " )

print (sistemaRecomendaciones(clima, horaDia))

## Hecho por Mateo Roman Camargo // TI 1.044.624.790