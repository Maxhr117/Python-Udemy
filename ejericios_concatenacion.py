# 1-Nombre completo
# Crea tres variables: nombre, apellido_paterno, apellido_materno.
# luego concatena y muestra el nombre completo.
from multiprocessing.util import close_all_fds_except

nombre = 'Max'
apellido_paterno = 'Hernandez'
apellido_materno = 'Ruiz'

nombre_completo = nombre + ' ' + apellido_paterno + ' ' + apellido_materno
print(nombre_completo)

# 2-Saludo personalizado
# Crea una variable nombre y otra hora. Luego muestra un saludo como:
# "Hola, Ana. Son las 10:00."

nombre2 = 'Rafa'
hora = '12:30'

print(f'Hola, {nombre2}. Son las {hora}.')

# 3-Unir elementos de una lista
# Tienes una lista de palabras ["Hola", "cómo", "estás"]. Únelas con un espacio y muestra la frase completa.
#
# Pista: usa " ".join(lista)

palabras = ['Hola ', 'como ', 'estas']
print(''.join(palabras))

# 4- Conversion y concatenacion
# Crea una variable edad = 25. Muestra la frase:
# "Tienes 25 años."
#
# ⚠️ Recuerda convertir el número a string.

edad = 25
conversion = str(edad)
print('Tienes ', edad, 'años')
print(type(conversion))

# 5-F-string avanzado
# Crea variables: nombre = "Luis", producto = "libro", precio = 300.
# Muestra el mensaje:
# Luis compró un libro por $300.
#
# Hazlo usando un f-string.
nombre3 = 'Luis'
producto = 'libro'
precio = 300

print(f'{nombre3} compro un {producto} por ${precio}')

# 6-Linea decorativa
# Usa el operador * para repetir una cadena.
# Ejemplo: print("=" * 30) debería mostrar:
# ==============================
espacios = "="
print(espacios * 35)
print("=" * 30)

# 7 tarjeta de presentacion
# Crea variables: nombre, profesion, ciudad.
# Muestra un mensaje como:
# "Hola, soy Carlos, soy Ingeniero y vivo en Bogotá."

# Puedes usar concatenación con + o f-strings.

nombre4 = 'Omar'
profesion = 'Electricista'
ciudad = 'Vancouver'

print(f'Hola, soy {nombre4}, soy {profesion} y vivo en {ciudad}.')

# 8 Formato de direccion
# Crea variables: calle, numero, colonia, ciudad.
# Muestra un mensaje como:
# "Tu dirección es: Av. Reforma 120, Col. Centro, Ciudad de México."
#
# Asegúrate de que haya espacios y comas correctamente.

calle = 'Juan Escutia'
numero = 6
colonia = 'Marco Antonio Munoz'
ciudad2 = 'Xalapa'

print(f'Tu direccion es: {calle} {numero}, Col. {colonia}, {ciudad2}')

# 9 Linea con nombre repetido
# Crea una variable nombre = "Valeria"
# Muestra el nombre 5 veces en la misma línea, separado por guiones:

nombre5 = 'Valeria'
print((''.join(nombre5) + '-') * 5)
