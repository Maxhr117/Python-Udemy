# El mayor de 2 numeros
"""
>Crear un programa para indicar cuál es el mayor de dos numeros.
>El programa debe pedir al usuario dos numeros enteros.
>Posteriormente, se deben comparar y mandar a imprimir el número mayor.
"""
numero1 = int(input('Ingresa un numero: '))
numero2 = int(input('Ingresa otro numero: '))

if numero1 > numero2:
    print(f'El numero mayor es: {numero1} ')
else:
    print(f'El numero mayor es: {numero2}')
