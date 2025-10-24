#--------------------------------------
# FUNCIONES LAMBDA
#--------------------------------------

def operaciones(operacion):
    if operacion == "suma":
        return lambda x,y : x + y
    elif operacion == "resta":
        return lambda x,y : x - y
    elif operacion == "multi":
        return lambda x,y : x * y
    else:
        return lambda x,y : x / y
suma = operaciones("suma")
print(suma(2,5))

#--------------------------------------

estudiantes = [
    {"nombre": "Juan", "edad": 30},
    {"nombre": "Jose", "edad": 20},
    {"nombre": "Julia", "edad": 40}
]
estudiantesOrdenados = sorted(estudiantes, key = lambda x: x["edad"])
print(estudiantesOrdenados)