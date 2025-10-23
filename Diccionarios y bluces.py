#---------------------------------
# DICCIONARIO [Coleccion no onrdenada de clave:valor]
#---------------------------------

diccionario = {
    "Nombre": "Jona",
    "Apellido": "Rdgz",
    "Edad": 34
}

#diccionario2 = diccionario.copy()
#diccionario2 = dict(diccionario)

for values in diccionario.values():
    print(values)

for x,y in diccionario.items():
    print(x)
    print(y)

for x,y in diccionario.items():
    print(x,y)