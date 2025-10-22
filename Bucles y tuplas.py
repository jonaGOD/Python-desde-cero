#------------------------------------
# TUPLAS [Coleccion de elementos inmutables y ordenados]
#------------------------------------

tupla = ("Manzana", "Banana", "Pera", "Mandarina", "Frutilla", "Anana")

for fruta in tupla:
    print(fruta)

for i in range(len(tupla)):
    print(tupla[i], "con el indice", i)

i = 0
while i < len(tupla):
    print(tupla[i])
    i += 1