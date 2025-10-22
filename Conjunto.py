#-----------------------
# SET (CONJUNTO) [Coleccion no ordenada y mutable de elementos unicos]
#-----------------------

conjuntoFruta = {"Manzana", "Banana", "Pera", "Mandarina", "Frutilla", "Anana"}
# Al no ser ordenados, no tiene indice por lo que no funcionaria el print(conjuntoFruta[1])
conjuntoBooleano = {True, False, 1, 0}
listaFruta = ["Kiwi", "Durazno"]

print(conjuntoFruta)
print(conjuntoBooleano) # Python toma el valor 0 como False y el 1 como True, no los imprime en pantalla ya que los considera valor duplicado.
print("Manzana" in conjuntoFruta)
conjuntoFruta.add("Limon")
print(conjuntoFruta)

conjuntoFruta.update(conjuntoBooleano)
print(conjuntoFruta)

conjuntoFruta.update(listaFruta)
print(conjuntoFruta)

conjuntoFruta.remove("Banana")
print(conjuntoFruta)
conjuntoFruta.discard("Pera")
print(conjuntoFruta)
