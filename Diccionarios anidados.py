#---------------------------------
# DICCIONARIO [Coleccion no onrdenada de clave:valor]
#---------------------------------

familia = {
    "Padre": {
        "Nombre": "Raul",
        "Profesion": "Ingeniero"
    },

    "Madre": {
        "Nombre": "Julieta",
        "Profesion": "CEO"
    },
    
    "Hijo": {
        "Nombre": "Pedro",
        "Profession": "Desempleado"
    }
}

print(familia["Padre"]["Profesion"])

for pariente, data in familia.items():
    print(pariente)
    for clave in data:
        print(clave + ":", data[clave])