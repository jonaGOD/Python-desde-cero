# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero
# e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

nombre = input("Ingrese su nombre: ")
repeticiones = int(input("Ingresa la cantidad de repeticiones: "))
i = 0

while i < repeticiones:
    print(nombre)
    i += 1