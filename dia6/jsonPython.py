import json

jsonString = '{"nombre": "Mateo", "apellido": "Roman", "edad": 17}' 

diccionarioPython = json.loads(jsonString)
print(diccionarioPython)
print(type(diccionarioPython))
print(diccionarioPython['nombre'])

diccionario = {"Juego": "League of legends",
                "Empresa": "Riot Games",
                "Fecha": 2008
              }
jSon = json.dumps(diccionario)
print(jSon)
print(type(jSon))