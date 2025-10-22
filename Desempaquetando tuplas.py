#------------------------------------
# TUPLAS [Coleccion de elementos inmutables y ordenados]
#------------------------------------

tuplaFruta = ("Manzana", "Banana", "Pera", "Mandarina", "Frutilla", "Anana")

(a, b, c, *d) = tuplaFruta # Desempaquetado de tupla en distintas variable

print(a)
print(b)
print(c)
print(d)

#------------------------------------

(a, *b, c) = tuplaFruta # Desempaquetado de tupla en distintas variable

print(a)
print(b)
print(c)