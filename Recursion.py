def sumaNaturales(n):
    if n == 1:
        return 1
    else:
        return n + sumaNaturales(n-1)
print(sumaNaturales(5))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

def suma(a,b):
    """
    Esta funcion suma dos numeros y devuelve el resultado.

    Args:
        a (int): Primer numero a sumar.
        b (int): Segundo numeor a sumar.

    Returns:
        int: La suma de los dos numeros
    """
    return a + b

help(suma)