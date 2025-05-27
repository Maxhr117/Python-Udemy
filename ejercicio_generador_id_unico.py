# Sistema Generador ID unico.
# Se solicita crear un sistema para generar un ID unico para cada persona.
# El sistema debe solicitar al usuario:
# Nombre
# Apellido
# Ano de nacimiento(yyyy)
# Con los datos recibidos del sistema debera realizar lo siguiente:
# 1- Del valor recibido de nombre, usar solo las 2 primeras letras y convertirlas a mayusculas
# 2- Del valor de apellido, usar las 2 primeras letras y convertirlas a mayusculas
# 3- Del valor de ano, tomar los 2 ultimos digitos.
# Ademas el sistema debera generar un valor aleatorio de 4 digitos, con ayuda de la funcion >randit<
# Finalmente, con los datos obtenidos generar un ID unico uniendo los valores como sigue:
# ejemplo :
# Nombre> Jose > JO
# Apellido> Perez > PE
# Ano Nacimiento> 1995 > 95
# Valor aleatorio > randit > 2352
# resultado ID unico: JOPE952352

import random

print("---Generador de ID unico---")
nombre = input('> Ingrese su nombre: ')
apellido = input('> Ingrese su apelido: ')
ano_nacimiento = (input('> Ingrese su ano de nacimiento completo: '))
numero = random.randint(1000, 9999)

print('----------------------')
print(f'Su ID unico es: ' + nombre.upper()[0:2] + apellido.upper()[0:2] + ano_nacimiento[-2:] + str(numero))
