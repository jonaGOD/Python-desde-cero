#--------------------------------------
# FUNCIONES DE ORDEN SUPERIOR
#--------------------------------------

def exterior(x):
    def interior(y):
        return x + y
    return interior

# CREAMOS UNA CLAUSURA LLAMANDO A LA FUNCION EXTERIOR
clausura = exterior(10)

# CUANDO LLAMEMOS A LA FUNCION CLAUSURA VA A RECORDAR EL VALOR QUE LE DIMOS
resultado = clausura(5)

print(resultado)