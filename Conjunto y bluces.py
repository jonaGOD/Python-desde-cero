#-----------------------
# SET (CONJUNTO) [Coleccion no ordenada y mutable de elementos unicos]
#-----------------------

set1 = {"Python", "AWS", "Java"}
set2 = {"Python", "Azure", "C++"}

set3 = set1.intersection(set2) # Muestra las diferencias de los conjuntos.
print(set3)

set3 = set1.difference(set2) # Muestra las diferencias de los conjuntos.
print(set3)

set1.intersection_update(set2)
print(set1)

#-----------------------

letras = {"a", "b", "c", "d"}
numeros = {"1", "2", "3", "4"}

union = letras | numeros
print(union)