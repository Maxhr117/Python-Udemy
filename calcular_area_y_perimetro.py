# Calculo Area y Perimetro de un rectangulo
""" Se solicita calcular el area y perimetro de un rectangulo aplicando
las siguientes formulas:
area = base * altura
perimetro = 2 * (base + altura)
*se le va solicitar al usuario los datos de base y altura"""

# solicitamos datos
base = float(input('Ingresa el valor de la base del rectangulo: >'))
altura = float(input('Ingresa el valor de la altura del rectangulo: >'))

# calculamos
area = base * altura
perimetro = 2 * (base + altura)
# mostramos resultado
print(f'El area es {area}m2.\nEl perimetro es {perimetro}m.')
