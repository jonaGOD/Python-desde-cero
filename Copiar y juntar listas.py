# INDICES
#         0(-6)      1(-5)     2(-4)   3(-3)          4(-2)     5(-1)
lista = ["Manzana", "Banana", "Pera", "Mandarina", "Frutilla", "Anana"]
lista2 = ["Lechuga", "Tomate", "Batata"]

copia = lista.copy()
print(copia)
copia2 = list(lista)
print(copia2)

copia3 = lista + lista2
print(copia3)

lista.extend(lista2)
print(lista)

print(lista.count("Banana"))
