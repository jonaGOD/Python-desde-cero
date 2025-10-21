nombre1 = input("Ingrese el nombre del Jugador 1: ")
nombre2 = input("Ingrese el nombre del Jugador 2: ")

jugador1 = input(nombre1 + " elige piedra, papel o tijera: ").lower()
jugador2 = input(nombre2 + " elige piedra, papel o tijera: ").lower()

condicion1 = (jugador1 == "piedra" and jugador2 == "tijera")
condicion2 = (jugador1 == "papel" and jugador2 == "piedra")
condicion3 = (jugador1 == "tijera" and jugador2 == "papel")

if jugador1 == jugador2:
    print("¡Empate!")
elif condicion1 or condicion2 or condicion3:
    ("El ganador es:", nombre1)
else:
    print("El ganador es:", nombre2)