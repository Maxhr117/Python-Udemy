dia_lluvioso = False
dia_nublado = False

# if dia_lluvioso == True:
#    print('Esta lloviendo, lleva paraguas.')
# elif dia_nublado == True:
#    print('Esta nublado, lleva impermeable.')
# else:
#    print('No lleves nada, deja todo en casa.')

# ejemplo 2

edad = int(input('Que edad tiene?: '))
viene_acompanado = str(input('Viene acompanado?: (si/no)'))

if edad >= 17:
    print('Bienvenido, adelante!')
    print('Se ejecuto la primera condicion.')
elif viene_acompanado.lower() == 'si':
    print('Puedes entrar con tus padres.')
    print('Se ejecuto la segunda condicion.')
else:
    print('Acceso denegado.')
    print('Se ejecuto el else.')
