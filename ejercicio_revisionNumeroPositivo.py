# Revisr si un numero es positivo

numero = int(input('Ingrese un numero: '))
if numero > 0:
    print(f'{numero} es positivo (+)')
elif numero < 0:
    print(f'{numero} es negativo (-)')
else:
    print(f'{numero} es cero.')
