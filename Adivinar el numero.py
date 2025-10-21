import random

numRandom = random.randint(1, 10)
numUsuario = int(input("Adivina un número entre 1 y 10: "))
adivino = False

for i in range(2):
    if numUsuario == numRandom:
        adivino = True
        break
    else:
        print("Número incorrecto. Intenta de nuevo.")
        numUsuario = int(input("Adivina un número entre 1 y 10: "))
if adivino:
    print("¡Felicidades! Has adivinado el número.")
else:
    print(f"Lo siento, no has adivinado el número. El número correcto era {numRandom}.")