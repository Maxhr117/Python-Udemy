# El metodo .find() en Python se usa para buscar la posicion de una subcadena dentro
# de una cadena mas grande.
# sintaxis basica:
# cadena.find(subcadena
# devuelve el indice(posicion) en donde COMIENZA la subcadena.
# si NO la encuentra, devuelve -1.

# Ejemplo:
frase = "Hola mundo desde Python"
posicion = frase.find('mundo')
print(posicion)
# 'mundo' empieza en el indice 5
# puedes usar ese numero para hacer slicing:
print(frase[posicion:posicion + 5])

frase = 'Python es lo mejor'
posicion = frase.find('lo')
print(posicion)
print(frase[posicion:posicion + 2])

frase = 'Un gran poder conlleva una gran responsabilidad'
posicion = frase.find('conlleva')
print(posicion)
print(frase[posicion:posicion + 8])

frase = 'Todos cometemos errores, eso nos hace humanos'
posicion = frase.find('hace')
print(posicion)
print(frase[posicion:posicion + 4])

# Usar .find() con espacios:
# Si quieres contar cuantas palabras hay o ubicar palabras separadas
# por espacios, puedes hacer algo como:

frase = 'Hello world from Python'
primera_palabra = frase[0:frase.find(" ")]  # Desde el inicio hasta el primer espacio
print(primera_palabra)

# si tu texto esta bien estructurado con espacios, puedes usar .split() para obtener directamente las palabras:
frase = 'Hello world from Python'
palabras = frase.split()  # ['Hello', 'world', 'from', 'Python']
print(palabras[2])  # from
