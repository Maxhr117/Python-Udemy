# Ejercicio 1 : Sofia queria ir al cine,pero solo puede entrar gratis si:
# Es menor de 12 anos,
# o
# Es mayor de 65 anos
# Escribir un programa que diga:
# "Entras gratis al cine!"
# "Tienes que pagar tu entrada"
print("---Sofia quiere entrar al cine---")
edad = 10
if edad >= 12 or edad <= 65:
    print('Entras al cine gratis!')
else:
    print('Tienes que pagar tu entrada.')
print()
# ejercicio 2: En una fiesta de halloween, solo puedes entrar si:
# tienes disfraz
# o
# tu nombre est en la lista VIP
# hacer que el programa diga:
# 'Bienvenido a la fiesta monstruosa!'
# o
# 'Lo siento! No puedes entrar sin disfraz ni invitacion!'
disfraz = False
on_list = False
if disfraz or on_list:
    print('Bienvenido a la fiesta monstruosa!')
else:
    print('Lo siento! No puedes entrar sin disfraz ni invitacion!')
print()
# ejercicio 3: Sistema prestamo de libros
# Se pide crear un sistema para una biblioteca, la cual desea
# prestar libros si cumple con cualquiera de las siguientes condiciones.
# El usuario tiene credencial de estudiante
# o
# El usuario vive a no mas de 3km a la redonda.
# Si cumple con cualquiera de estas condiciones se le puede prestar el libro.
credencial = True
distancia = 5  # en km
if credencial or distancia <= 3:
    print('Se le puede prestar el libro.')
else:
    print('No se te puede prestar el libro.')

distancia_permitida_km = 3
tiene_credencial = input('Cuentas con credencial de estudiante? (Si/No) ')
distancia_biblioteca_km = int(input('A cuantos km vives de la biblioteca?'))

es_elegible_prestamo = (tiene_credencial.lower() == 'si'
                        or distancia_biblioteca_km <= distancia_permitida_km)
print(f'Eres elegible para prestamo de libro?{es_elegible_prestamo}')
