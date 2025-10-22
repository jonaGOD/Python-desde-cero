# INDICES
#         0(-6)      1(-5)     2(-4)   3(-3)          4(-2)     5(-1)
lista = ["Manzana", "Banana", "Pera", "Mandarina", "Frutilla", "Anana"]
numeros = [1,3,5,7,9,2,4,6,8]
listaMinusc = ["Manzana", "Banana", "Pera", "mandarina", "frutilla", "Anana"]

lista.sort() 
print(lista)
numeros.sort()
print(numeros)

lista.sort(reverse=True)
print(lista)
numeros.sort(reverse=True)
print(numeros)

listaMinusc.sort()
print(listaMinusc)
listaMinusc.sort(key=str.lower)
print(listaMinusc)