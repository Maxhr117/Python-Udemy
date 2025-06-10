# Usar un ciclo while para imprimir los numeros del 1 al  20
contador = 1
while contador <= 5:
    contador += 1
    print(f"Contando:  {contador}")

print("-------------------------------------------------")
# Adivinar el numero secreto.
# El programa tiene un numero secreto y el usuario tiene que adivinarlo. El ciclo sigue hasta que
# adivine correctamente.

numero_secreto = 55
adivinar = int(input("> Adivina el numero secreto: "))

while adivinar != numero_secreto:
    print("> Numero equivocado, intenta de nuevo.")
    adivinar = int(input("> intenta de nuevo: "))
print("Correcto! adivinaste el numero secreto.")

print("-------------------------------------------------")

# El usuario tiene que adivinar un numero secreto. pero esta vez, el programa le dice si su intento fue
# demasiado alto o demasiado bajo, para ayudarlo a acercarse.

numero_secreto = 77
numero_ingresado = int(input("> Adivina el numero secreto! :  "))

while numero_ingresado != numero_secreto:
    if numero_ingresado < numero_secreto:
        print("Demasiado bajo.")
    elif numero_ingresado > numero_secreto:
        print("Demasiado alto.")
    numero_ingresado = int(input("> Adivina el numero secreto! :  "))
print("Correcto , adivinaste !")
