# ejercicios integrados que combinan varios temas ya vistos:
# Temas cubiertos: Declaracion de variables, Tipos de datos, Cadenas y subcadenas,
# concatenacion, metodos de cadenas, slicing

# 🧪 Ejercicio 1: Nombre con formato
# Objetivo: Usar concatenación y métodos de cadenas.
# Instrucciones:
# Crea variables: nombre = "luis", apellido = "ramírez".
# Une ambos en una variable nombre_completo.
# Muestra el nombre completo en:
# Mayúsculas
# Minúsculas
# Formato título (cada palabra capitalizada)

nombre = 'lUiS'
apellido = 'raMIrEz'
nombre_completo = nombre + ' ' + apellido
print(nombre_completo)
print('Mayusculas:', nombre_completo.upper())
print('Minusculas:', nombre_completo.lower())
print('Titulo:', nombre_completo.title())

# 🧪 Ejercicio 2: Subcadenas y búsqueda
# Objetivo: Usar .find() y slicing.
# Instrucciones:
# Define frase = "Aprender Python es divertido".
# Encuentra la posición de la palabra "Python" en la frase.
# Usa slicing para extraer esa palabra con su posición.
print()
frase = 'Aprender Python es divertido'
posicion = frase.find('Python')
print(posicion)
print(frase[posicion:posicion + 6])

# 🧪 Ejercicio 3: Separar y contar palabras
# Objetivo: Usar .split() y len().
# Instrucciones:
# Usa esta frase:
# "Los ejercicios ayudan a practicar programación"
# Separa las palabras en una lista.
# Muestra cuántas palabras hay
print()
frase = 'Los ejercicios ayudan a practicar programacion'
palabras = frase.split()  # primero hacer una funcion para separar las palabras
print(palabras)
cantidad_palabras = len(palabras)  # despues una funcion para contar esas palabras ya separadas
print('La frase contiene ', cantidad_palabras, 'palabras.')

# 🧪 Ejercicio 4: Invertir nombre
# Objetivo: Usar slicing con paso negativo.
# Instrucciones:
# Crea una variable nombre = "Carlos".
# Muestra el nombre invertido: 'solraC'.
print()
nombre = 'Carlos'
print(nombre)
print('Nombre invertido: ', nombre[::-1])

# 🧪 Ejercicio 5: Formato de dirección
# Objetivo: Practicar concatenación y uso de .title().
# Instrucciones:
# Crea las variables:
# calle = "av. independencia"
# numero = "123"
# ciudad = "méxico"
# Une todo en una sola cadena con este formato:
# "Av. Independencia 123, México"
# (usa .title() donde sea necesario)
print()
calle = 'Av. independencia'
numero = '123'
ciudad = 'mexico'
direccion = f'{calle} {numero} {ciudad}'
print(direccion.title())

# 🧪 Ejercicio 6: Iniciales del nombre
# Objetivo: Usar slicing para extraer iniciales.
# Instrucciones:
# Crea estas variables:
# nombre = "Roberto"
# apellido = "Martínez"
# Extrae y muestra las iniciales en mayúsculas: "R.M."
print()
nombre = 'Roberto'
apellido = 'Martinez'
nombre_completo = f'{nombre} {apellido}'
print(nombre_completo)
print(nombre[0:1], apellido[0:1])

# 🧪 Ejercicio 7: Revisar si contiene una palabra
# Objetivo: Usar .find() y condicional simple.
# Instrucciones:
# Define la frase: "Estoy aprendiendo programación en Python".
# Pregunta al usuario una palabra.
# Verifica si la palabra se encuentra en la frase usando .find() o el operador in.
# Muestra un mensaje indicando si la palabra fue encontrada.
print()
frase = 'Estoy aprendiendo programacion en Python'
print(frase)
palabra = input('ingresa una palabra: ')
palabras = frase.split()
print(palabras)
if palabra in palabras:
    print('Encontraste la palabra')
else:
    print('Ninguna palabra encontrada')
# 🧪 Ejercicio 8: Contar letras y espacios
# Objetivo: Usar len() y .count().
# Instrucciones:
# Define la cadena: "Python es poderoso y divertido".
# Muestra:
# La cantidad total de caracteres.
# Cuántos espacios contiene.
# 💡 Usa .count(" ") para contar espacios.
print()
cadena = 'Python es poderoso y divertido.'
print(cadena)
longitud_de_cadena = len(cadena)
cantidad_espacios = cadena.count(" ")

print('Contiene: ', longitud_de_cadena, 'caracteres y ', cantidad_espacios, 'espacios.')

# 🧪 Ejercicio 9: Reemplazar palabras
# Objetivo: Usar .replace().
# Instrucciones:
# Frase original: "La programación es difícil".
# Reemplaza "difícil" por "fácil" y muestra el resultado.
print()
frase_original = 'La programacion es dificil'
reemplazo = frase_original.replace('dificil', 'facil')  # la variable reemplazo va a sustituir
# a frase_original y se le va a aplicar el metodo .replace() el cual va a tomar como primer valor la
# subcadena que se desea cambiar 'dificil' como primer valor, y como segundo valor la subcadena nueva.
print(reemplazo)

# 🧪 Ejercicio 10: Mostrar solo vocales
# Objetivo: Usar slicing y condicionales.
# Instrucciones:
# Frase: "Aprender Python".
# Recorre la cadena con un for.
# Muestra solo las vocales (minúsculas o mayúsculas).
# Pista: Usa if letra.lower() in "aeiou"
print()
frase = 'Aprender Python'  # primero definir la frase, guardamos al cadena en una variable
for letra in frase:  # recorremos la frase letra por letra con un for
    if letra.lower() in 'aeiou':  # convertir cada letra a minuscula y verificar si es una vocal
        print(letra)  # imprimir al vocal
