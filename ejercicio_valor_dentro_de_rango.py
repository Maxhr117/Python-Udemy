# Valor Dentro de Rango
"""Solicitar al usuario un valor entre 0 y 5 e indicarle
si el valor proporcionado esta dentro de rango.

Se deben definir 2 constantes, VALOR_MINIMO = 0 y VALOR_MAXIMO = 5

Y debemos comprobar si el valor proporcionado se encuentra en el rango
entre 0 y 5

Finalmente se debe imprimir:
valor dentro de rango: True/False """

# definir constantes
valor_minimo = 0
valor_maximo = 5
valor_usuario = int(input('Ingrese un valor entre 0 y 5:'))

# comprobacion solucion1

# if valor_usuario >= valor_minimo and valor_usuario <= valor_maximo:
#    print(True)
# else:
#    print(False)

# comprobacion solucion2
en_rango = valor_minimo <= valor_usuario <= valor_maximo
print(f'El valor esta dentro de rango?: {en_rango}')
