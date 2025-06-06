# Sistema de calificaciones
"""Crear un programa para convertir una calificación numerica (entre 0 y 10)
a una letra (de la F a la A)
Si es mayor o igual a 9 y menor o igual a 10 es una A
Si es mayor o igual a 8 y menor a 9 es una B
Si es mayor o igual a 7 y menor a 8 es una C """
print('---Sistema de calificaciones---')
calificacion = float(input('Ingresa la califiacion con numero (0-10: '))
if calificacion >= 9 or calificacion == 10:
    print('Obtienes una "A".')
elif calificacion >= 8 or calificacion < 9:
    print('Obtienes una "B".')
elif calificacion >= 7 or calificacion < 8:
    print('Obtienes una "C".')
elif calificacion >= 6 or calificacion < 7:
    print('Obtienes una "D".')
elif calificacion >= 0 or calificacion < 6:
    print('REPROBADO.')
else:
    print('Valor incorrecto.')

# opcion 2
print()
calificacion2 = float(input('Ingresa la califiacion con numero (0-10: '))
calificacion_enLetra = ''
if calificacion2 >= 9 or calificacion2 == 10:
    calificacion_enLetra = 'A'
elif calificacion2 >= 8 or calificacion2 == 9:
    calificacion_enLetra = 'B'
elif calificacion2 >= 7 or calificacion2 == 8:
    calificacion_enLetra = 'C'
elif calificacion2 >= 6 or calificacion2 == 7:
    calificacion_enLetra = 'D'
elif calificacion2 >= 0 or calificacion2 == 5:
    calificacion_enLetra = 'F (REPROBADO)'
else:
    calificacion_enLetra = 'VALOR INCORRECTO.'
print(f'Tu calificacion {calificacion2} corresponde a la letra {calificacion_enLetra}.')
