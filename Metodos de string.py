texto = "HoLa MuNdO"
textoEspaciado = "  Texto con Espacios   "
textoSeparado = "Python,Java,Django"
lista = ["Hola", "Juan", "Carlos"]
numeros = "12345"
espacio = " "
repeticion = "Manzana, Naranja, Manzana, Limon"

print("Capitalize:", texto.capitalize()) # Convierte la primera letra en MAYUS y el resto en minusc.
print("Upper:", texto.upper()) # Convierte el texto en MAYUS.
print("Upper:", texto.lower()) # Convierte el texto en minusc.
print("Strip:", textoEspaciado.strip()) # Elimina espacios al inicio y al final.
print("Strip:", textoEspaciado.replace("Espacios", "¿Que lees?")) # Elimina espacios al inicio y al final.
print("Split:", textoSeparado.split(",")) # Seperar texto en items de una lista.
print("Join:", ",".join(lista)) # Junta los items de una lista en un String.
print("Find:", texto.find("MuNdO")) # Indica el indice/posicion donde inicia el texto ingresado.
print("RFind:", repeticion.rfind("Manzana")) # Indica la última posición en la que se encuentra el texto ingresado.
print("Index", texto.index("MuNdO")) # Indica el indice/posicion donde inicia el texto ingresado.
print("Start with:", texto.startswith("Adios")) # Indica si comienza o no con la palabra ingresada.
print("Start with:", texto.startswith("HoLa")) # Indica si comienza o no con la palabra ingresada.
print("Ends with:", texto.endswith("Adios")) # Indica si finaliza o no con la palabra ingresada.
print("Ends with:", texto.endswith("MuNdO")) # Indica si finaliza o no con la palabra ingresada.
print("In digit:", numeros.isdigit()) # Indica si todos los caracteres son numeros o no. (Considera epsacios)
print("Is alpha:", numeros.isalpha()) # Indica si todos los caracteres son letras o no. (Considera epsacios)
print("Is space:", texto.isspace()) # Indica si el string solo esta hecho de espacios.
print("Is space:", espacio.isspace()) # Indica si el string solo esta hecho de espacios.
print("Count", repeticion.count("Manzana")) # Indica cuantes veces se repite la palabra ingresada.