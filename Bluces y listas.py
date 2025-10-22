# INDICES
#         0(-6)      1(-5)     2(-4)   3(-3)          4(-2)     5(-1)
lista = ["Manzana", "Banana", "Pera", "Mandarina", "Frutilla", "Anana"]

[print(lista) for lista in lista]

for i in range(len(lista)): # Len mide la longitud.
    print(lista[i])

i = 0
while i < len(lista):
    print(lista[i])
    i += 1