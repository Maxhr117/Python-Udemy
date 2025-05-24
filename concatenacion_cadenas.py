# Concatenacion de cadenas
cadena1 = 'Hola'
cadena2 = 'Mundo'

concatenacion = cadena1 + " " + cadena2

print(concatenacion)

# usando el metodo join() (para listas de cadenas
palabras = ['Hola', ' ', 'buenos', ' ', 'dias']
frase = ''.join(palabras)
print(frase)

# Usando f-strings(recomendado en Python 3.6+)

nombre = 'Dante'
edad = 33
print(f'Hola, {nombre}. Tienes {edad} anos.')

# usando .format()
nombre = 'Vanessa'
edad = 21
print('Bienvenida, {}!'.format(nombre), ' tienes {}!'.format(edad), 'años')
# Tambien utilizando indices o nombres:
print('Hola, {0}. Tienes {1} años.'.format('Pedro', 20))
