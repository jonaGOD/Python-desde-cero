#------------------------------------
# TUPLAS [Coleccion de elementos inmutables y ordenados]
#------------------------------------

#         0(-6)       1(-5)     2(-4)    3(-3)       4(-2)      5(-1)
tupla = ("Manzana", "Banana", "Pera", "Mandarina", "Frutilla", "Anana")
tupla2 = list(tupla) # Convierte la Tupla a lista.
tupla3 = ("Lechuga", "Tomate", "Ajo")

tupla2[1] = "Narajna" # Modifica el valor de la asignacion indicada.
tupla = tuple(tupla2) # Convierte la lista en una tupla y la reasigno la variable original.
print(tupla2)

tupla2 = list(tupla) # Convierte la Tupla a lista.
tupla2.append("Coco") # Agrega el valor indicado.
tupla = tuple(tupla2) # Convierte la lista en una tupla y la reasigno la variable original.
print(tupla2)

tupla += tupla3 # Concatenacion.
print(tupla)

del tupla
#print(tupla)