# longitud de una cadena
# Para obtener el largo (número de caracteres) de una cadena en Python, se usa la función incorporada len().
#   len(nombre_de_la_cadena)

cadena = 'hoLa muNdo'
longitud = len(cadena)
print(cadena)
print(longitud)
print(cadena.upper())
print(cadena.lower())

nombre6 = 'ivan'
print(f'Bienvenido {nombre6.upper()}')

# convertir a mayusculas .upper()
texto = 'hola mundo'
mayusculas = texto.upper()
print(texto)
print(mayusculas)

# convertir a minusculas .lower()
texto2 = 'HOLA MUNDO!'
minusculas = texto2.lower()
print(texto2)
print(minusculas)

# Capitalizar(primera letra en mayusculas): .capitalize()
texto3 = 'hello world'
caps = texto3.capitalize()
print(texto3)
print(caps)

# capitalizar CADA PALABRA  .title()
texto4 = 'max hernandez ruiz'
primer_letra = texto4.title()
print(texto4)
print(primer_letra)

# usando todos juntos

texto5 = 'pYtHoN eS gEnIaL'
print('original > ' + texto5)
print('lower > ' + texto5.lower())
print('upper > ' + texto5.upper())
print('capitalize > ' + texto5.capitalize())
print('title > ' + texto5.title())
