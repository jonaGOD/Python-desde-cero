def division(dividendo, divisor):
    try:
        resultado = dividendo / divisor
        return resultado
    except ZeroDivisionError:
        print("No se puede dividir por 0")
        resultado = None
    return resultado

print(division(5,0))
print("El programa se sigue ejecutando")