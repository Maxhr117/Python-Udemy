print("*** Bienvenidos al sistema bancario ***")

salir_sistema = input('> Deseas SALIR del sistema (si/no) ?')

if not salir_sistema == 'si':
    print('> Continuamos dentro del sistema...')
elif not salir_sistema == 'no':
    print('> Saliendo del sistema...')
else:
    print('')
