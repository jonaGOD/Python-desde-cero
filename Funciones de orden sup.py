#--------------------------------------
# FUNCIONES DE ORDEN SUPERIOR
#--------------------------------------

numeros = [1, 2, 3, 4, 5, 6]

cuadrado = list(map(lambda x: x*x, numeros))
pares = list(filter(lambda x: x % 2 == 0, numeros))

print(cuadrado)
print(pares)