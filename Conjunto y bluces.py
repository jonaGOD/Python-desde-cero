#-----------------------
# SET (CONJUNTO) [Coleccion no ordenada y mutable de elementos unicos]
#-----------------------

set1 = {"Python", "AWS", "Java"}
set2 = {"Python", "Azure", "C++"}

set3 = set1.intersection(set2)
print(set3)

set3 = set1.difference(set2)
print(set3)

set1.intersection_update(set2)
print(set1)

