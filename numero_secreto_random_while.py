# El programa genera un numero secreto y tienes que adivinarlo
import random

numero_secreto = random.randint(1, 10)
intento = 0
adivinanza = 0

while adivinanza != numero_secreto:
    adivinanza = int(input("Intenta adivinar el numero secreto: "))
    intento += 1
    if adivinanza < numero_secreto:
        intento += 1
        print("Muy bajo..")
    elif adivinanza > numero_secreto:
        print("Muy alto..")
print(f"Muy bien ! Lo lograste en {intento} intentos !")
