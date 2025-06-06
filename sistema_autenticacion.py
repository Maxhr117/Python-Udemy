# Sistema de Autenticacion
"""
    Crear un sistema para validar los valores de usuario y password proporcionados
*Se deben definir dos constantes con los valores validos de usuario y password
Y  el sistema debe comparar los valores validos contra los valores proporcionados
Se debe considerar 4 casos:
1. Usuario y password validos. Debe imprimir 'Bienvenido al sistema'
2.Usuario invalido
3.Password invalido
4.Usuario y password invalidos.
"""
print('---Sistema de Autenticacion---')
usuario_valido = str('Admin')
password_valido = '123456'
usuario = str(input('>Ingresar nombre de usuario: '))
password = input('>Ingresar password: ')
print('---Validando..')
if usuario == usuario_valido and password == password_valido:
    print('>Usuario y Password validos \n---Bienvenido al sistema---.')
elif usuario != usuario_valido and password == password_valido:
    print('>Usuario invalido.')
elif usuario == usuario_valido and password != password_valido:
    print('>Password invalido.')
else:
    print('>Usuario y Password invalidos.')
