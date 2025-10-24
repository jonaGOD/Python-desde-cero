#--------------------------------------
# FUNCIONES COMO ARGUMENTOS / CALLBACKS
#--------------------------------------

def aplicarFuncion(func, valor):
    return func(valor)

def cuadrado(x):
    return x*x

def cubo(x):
    return x * x * x

print(aplicarFuncion(cuadrado,3))
print(aplicarFuncion(cubo,3))
