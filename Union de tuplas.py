#------------------------------------
# TUPLAS [Coleccion de elementos inmutables y ordenados]
#------------------------------------

tupla1 = ("Manzana", "Banana", "Pera")
tupla2 = ("Mandarina", "Frutilla", "Anana")

print(tupla1)
tupla1 = tupla1 + tupla2
print(tupla1)
tupla1 = (tupla1 * 2)+ tupla2
print(tupla1)
print(tupla1.count("Banana"))