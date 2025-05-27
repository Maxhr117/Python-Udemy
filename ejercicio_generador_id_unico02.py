# crea un programa que genere un ID de usuario con los siguientes valores:
# Nombre: dos ultimas letras en mayusculas segudas de un numero aleatorio de un solo digito
# Apellido paterno: dos ultimas letras en mayusculas segudas de un numero aleatorio de 2 digitos
# Apellido materno: dos ultimas letras en mayusculas segudas de un numero aleatorio de 2 digitos
import random

print('---Bienvenido a tu generador de ID unico---')
nombre = input(">Por favor ingresa tu nombre: ")
apellido_paterno = input(">Por favor ingresa tu apellido paterno: ")
apellido_materno = input(">Por favor ingresa tu apellido materno: ")
print(f'>Aqui tienes tu ID unico: ' + nombre[-2:] + str(random.randint(10, 90)) + apellido_paterno[-2:]
      + str(random.randint(0, 9)) + apellido_materno[-2:] + str(random.randint(0, 9)))
