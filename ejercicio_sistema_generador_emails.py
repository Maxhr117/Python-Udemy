# Sistema Generador Emails
# Se solicita crear un sistema para generar un email segun los datos recibidos. Se debe solicitar
# lo siguiente:
# 1-Nombre
# 2-Apellido
# Con estos datos se debe generar un email como sigue
# Nombre > Jose > convertir a minusculas
# Apellido > Jimenez > convertir a minusculas
# resultado ejemplo: jose.jimenez@etc..com

print('===>Bienvenido al Generador de Emails<===')
nombre = input('Ingresa tu nombre: ')
apellido = input('Ingresa tu apellido: ')
correo = nombre.lower() + "." + apellido.lower() + "@empresa.python"
print(f'Su nuevo correo generado es > {correo}')
