# Escribir un programa que pida al usuario dos números enteros y muestre
# por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> 
# son los números introducidos por el usuario, y <c> y <r> son 
# el cociente y el resto de la división entera respectivamente.

num1 = int(input("Ingrese el primer numero entero: "))
num2 = int(input("Ingrese el segundo numero entero: "))

resultado = num1 / num2
resto = num1 % num2

print(num1, "entre", num2, "da un cociente", resultado, "y", resto, "son el cociente y el resto de la division.")