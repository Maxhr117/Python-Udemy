# Tipos de ciclos en Python
# For: Este es el ciclo que usas cuando sabes cuantas veces quieres repetir algo o cuando estas recorriendo
# una coleccion (como una lista, un string, un rango, etc.)

i = 0
for i in range(11):
    print(i)

# range(5) genera los numeros del 0 al 10
# En casa vuelta, i tomaun valor diferente.
# Imprime el numero de vuelta

print()
# While: Este ciclo sigue repitiendo mientras una condicion sea verdadera(True).
contador = 0
while contador < 5:
    print('Contando estrellas', contador)
    contador += 1
# > Mientras contador sea menor que 5..
# > Imprimir el mensaje.
# > Suma 1 al contador.
# pero ojo ! si olvidas cambiar la condicion, podrias entrar en un bucle infinito.
print()
# palbras clave.
# break: rompe el hechizo, detiene el ciclo.
# continue: salta al siguiente verso, omite lo que queda de la vuelta actual.
# ejemplo con break:
for letra in "murcielago":
    if letra == "e":
        break
    print(letra)

print()
# Ejemplo con continue:
for numero in range(5):
    if numero == 2:
        continue
    print(numero)

# Cuando usar cual?
# | Situación                                              | Ciclo ideal |
# | --------------------------- | ----------- |
# | Sabés cuántas veces repetir |           `for`       |
# | Repetís mientras algo pase  |           `while`     |
# | Recorrés listas, strings    |                   `for`       |
# | Esperás a que algo cambie   |              `while`     |
