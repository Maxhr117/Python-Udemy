# Programa Mayor Edad
"""Crea un programa para saber si una persona es mayor de edad.
Utiliza una constante para indicar el valor cuando una persona se considera mayor de edad.
>Una persona se considera mayor de edad si ha cumplido 18 años.
Si es mayor de edad debe imprimir:
>La persona con X años es mayor de edad
Si es menor de edad debe imprimir:
>La persona con X años es menor de edad."""
print('---Programa Mayor Edad---')
edad = int(input('Ingresa tu edad: '))
mayor_edad = 18
if edad >= mayor_edad:
    print(f'La persona con {edad} años es mayor de edad.')
elif edad < mayor_edad:
    print(f'La persona con {edad} años es menor de edad.')
else:
    print('Valor no reconocido.')
