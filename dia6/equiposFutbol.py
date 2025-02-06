equiposFut={
    "1":{
        "nombre":"Stars",
        "plataforma":"Windows",
        "cantInte":5,
        "skins":["Goku","Sayayin","Barney"],
        "integrantes":[{"nombre":"Pedro","apellido":"Gomez","edad":24},{"nombre":"Aura","apellido":"Pico","edad":16}]
    },
    "2":{},
    "3":{}
}

booleanito = True
while(booleanito==True):
    print("############################")
    print("#####---Fut---#######")
    print("############################")
    print("¿A que equipo te gustaria ingresar?")
    print("1. Equipo 1")
    print("2. Equipo 2")
    print("3. Equipo 3")
    opt=input(":")
    if(opt=="1"):
        print("¿Qué te gustaría hacer adentro de los equipos?")
        print("1.Skins")
        opt2=int(input(":"))
        if (opt2==1):
            print("¿Qué te gustaría hacer con los skins?")
            print("1.Verlos")
            print("2.Agregar uno nuevo")
            print("3.Modificar uno")
            print("4.Eliminar uno")
            opt3=int(input(":"))
            if(opt3==1):
                print("############################")
                print("#####---Skins Disponibles---#######")
                print("############################")
                for i in range(len(equiposFut[opt]["skins"])):
                    print(equiposFut[opt]["skins"][i])
                print("############################")
            elif(opt3==2):
                nuevoSkin=input("¿Como se llama el nuevo skin?:")
                equiposFut[opt]["skins"].append(nuevoSkin)
                print("Skin agregado")
