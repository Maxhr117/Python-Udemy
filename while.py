# while repite un bloque de codigo mientras se cumpla una condicion.
# while condicion :
# codigo que se repite
# "Mientras esta condicion sea verdadera, sigue ejecutando esto."
# ejemplo.
contador = 1  # 1- comienza con contador = 1.
while contador <= 5:  # pregunta: contador <= 5?
    print(f"Contando: {contador}")  # si la respuesta es si, entra al bucle. # imprime el numero
    contador += 1  # y suma 1 al contador

# vuelve a preguntar hasta que la condicion ya no sea verdadera (cuando contador es 6)
# Ojo, si te olvidas de actualizar la condicion, el bucle puede convertirse en un bucle infinito
print("-----------------------")
# ejemplo:
suma = 0
numero = int(input("Ingresa un numero (0 para salir): "))

while numero != 0:
    suma += numero
    numero = int(input("Ingresa un numero (0 para salir): "))
print(f"La suma total es: {suma} ")

# cunado usar WHILE en vez de FOR: ?
# for: sabes cuantas veces repetiras algo. - iteras sobre una secuencia(lista,etc.)
# while: No sabes cuantas veces exactamente. - Repetis mientras algo sea verdadero.
