#----------------------------------
# FUNCION 
# Bloque de codigo reutilizable para realizar una tarea especifica.
#----------------------------------
# SINTAXSIS
#----------------------------------
# def nombreDeLaFuncion(parametros)
#   docstring de la funcion
#   cuerpo de la funcion
#   puede contener 1 o mas lineas de codigo
#   return resultdo
#----------------------------------

def saludar(nombre, apellido = "Rdgz"):
    print("Hola", nombre, apellido)

saludar("Jona")

def mercaderia(productos):
    for item in productos:
        print(item)

frutas = ["Manaza", "Banana", "Mandarina"]
mercaderia(frutas)


def operaciones(a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b !=0:
        division = a * b
    else:
        division = "No se puede divir por 0"
    return (suma, resta, multiplicacion, division)

print(operaciones(5,0))