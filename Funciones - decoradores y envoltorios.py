def decorador(funcion):
    def envoltorio():
        print("Esta funcionalidad se dispararía antes de la funcion que nos pasen por argumento")
        funcion()
        print("Esta funcionalidad se dispararía después de la funcion que nos pasen por argumento")
    return envoltorio

def saludar():
    print("Hola, estoy saludando")

saludo_decorado = decorador(saludar)
saludo_decorado()