#-----------------------
# LISTAS
#-----------------------

# INDICES
#         0(-6)      1(-5)     2(-4)   3(-3)          4(-2)     5(-1)
lista = ["Manzana", "Banana", "Pera", "Mandarina", "Frutilla", "Anana"]
lista2 = ["Tomate", "Lechuga"]

print(lista)
print(lista[0])
print(lista[-1])
print(lista[2:5])
print(lista[:5])
print(lista[-5:-2])

if "Sandia" in lista:
    print("Sandia esta en la lista")
else:
    print("Sandia no esta en la lista")

if "Banana" in lista:
    print("Banana esta en la lista")

lista[0] = "Banana"
lista[4:] =  ["Anana", "Frutilla"]
lista.insert(2, "Palta")
print(lista)
lista.extend(lista2) # Tambien puede hacerse con Tuplas.
print(lista)