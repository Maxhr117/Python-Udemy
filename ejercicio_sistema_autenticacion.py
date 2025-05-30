# Crea un programa para validar el usuario y password proporcionados por el usuario.

# Crea 2 constantes con los valores correctos y posteriormente compara que
# el usuario y password proporcionados sean validos.

# Debe solicitar el usuario y el password al usuario y, si son iguales que los valores almacenados en
# las constantes entonces debe imprimir True, de lo contrario debe imprimir False.
print('***Sistema de Autenticacion***')

# Crear constantes con valores
usuario = 'Anakin'
password = 'jedi123'

ingrese_usuario = input('Por favor ingrese nombre de usuario.')
ingrese_password = input('Por favor ingrese nombre de usuario.')
if ingrese_usuario == usuario and ingrese_password == password:
    print(True)
else:
    print(False)
