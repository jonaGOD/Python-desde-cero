#---------------------------------
# DICCIONARIO [Coleccion no onrdenada de clave:valor]
#---------------------------------

diccionario = {
    "Nombre": "Jona",
    "Apellido": "Rdgz",
    "Edad": 34
}

print(diccionario)
print(diccionario["Edad"])

nombre = diccionario.get("Nombre")
print(nombre)

claves = diccionario.keys()
print(claves)

items = diccionario.items()
print(items)

diccionario["Nombre"] = "Jonny"
diccionario["Pais"] = "ARG"
print(diccionario)

diccionario.update({"Nombre": "Jonathan"})
print(diccionario)

diccionario.pop("Pais")
print(diccionario)

diccionario.clear()
print(diccionario)

del diccionario