# Identifica la estación del año
""""Se solicita proporcionar el valor de un mes (valor numerico entre 1 y 12), e indicar la
estación del año según lo siguiente:
>Meses 1, 2 o 12 -> invierno
>Meses 3, 4 o 5 -> primavera
>Meses 6, 7 u 8 -> verano
>Meses 9, 10 u 11 -> otoño
>Cualquier otro valor : estacion desconocida"""
print('---Identifica la estación del año---')

# Opcion 1
estacion = int(input('Proporciona un valor entre 1 y 12 (meses) para identificar la estacion del ano: '))
if estacion in [1, 2, 12]:
    print('INVIERNO.')
elif estacion in [3, 4, 5]:
    print('PRIMAVERA')
elif estacion in [6, 7, 8]:
    print('VERANO')
elif estacion in [9, 10, 11]:
    print("OTOÑO")
else:
    print("Estación desconocida")

print()

# opcion 2
mes = int(input('Proporciona el valor del mes (1-12: '))
estacion_2 = ''
# Revision del mes proporcionado
if mes == 1 or mes == 2 or mes == 12:
    estacion_2 = 'Invieron'
elif mes == 3 or mes == 4 or mes == 5:
    estacion_2 = 'Primavera'
elif mes == 6 or mes == 7 or mes == 8:
    estacion_2 = 'Verano'
elif mes == 9 or mes == 10 or mes == 11:
    estacion_2 = 'Otoño'
else:
    estacion_2 = 'Estacion desconocida'
# imprimir resultado
print(f'La estacion que corresponde al numero {mes} es : {estacion_2}')
