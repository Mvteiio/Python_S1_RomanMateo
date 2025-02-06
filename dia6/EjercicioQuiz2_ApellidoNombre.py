# Estoy es pero perdido 
inmueblesDiccionario = {"inmuebles": [
                            {'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
                            {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
                            {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
                            {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
                            {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}
                        ]
                        }

def mostrarInmuebles ():
    for i in range (len(inmueblesDiccionario['inmuebles'])):
        print(inmueblesDiccionario['inmuebles'][i])



print (mostrarInmuebles())
