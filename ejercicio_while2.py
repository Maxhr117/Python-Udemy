import random

# objetivo
# Genere un numero secreto aleatorio entre 1 y 100.
# pedir al usuario que  adivine el numero..
# debe decir si el numero ingresado es muy alto, muy bajo o correcto.
# cuente los intentos.
# Al final, decir cuantos intentos uso.
# se usara import random, while y un contador para los intentos.

num_random = int(random.uniform(1, 100))
contador = 1
adivinar_numero = int(input("> Adivina el numero secreto entre 1 y 100: "))
while adivinar_numero != num_random:
    contador = contador + 1
    if adivinar_numero < num_random:
        print(f"{adivinar_numero} > es muy bajo.")
    elif adivinar_numero > num_random:
        print(f"{adivinar_numero} > es muy alto.")
    else:
        print("Valor no admitido.")
    adivinar_numero = int(input("> intenta de nuevo:  "))
print("Correcto, adivinaste !")
print(f"lo lograste en {contador} intentos")
