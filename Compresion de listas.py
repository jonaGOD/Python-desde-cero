# INDICES
#         0(-6)      1(-5)     2(-4)   3(-3)          4(-2)     5(-1)
lista = ["Manzana", "Banana", "Pera", "Mandarina", "Frutilla", "Anana"]
lista_con_e = [fruta for fruta in lista if "e" in fruta]
lista_con_i = [fruta for fruta in lista if "i" in fruta]

lista2 = [fruta if fruta != "Pera" else "Palta" for fruta in lista]

print(lista_con_e)
print(lista_con_i)
print(lista2)