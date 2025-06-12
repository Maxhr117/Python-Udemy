# imprime los numeros del 1 al 20 pero solo si son impares usando range
print(">impares  con range<")
for i in range(1, 20, 3):
    print(i)
print("-----------------------------------")
# pares con range
print(">pares con range<")
for i in range(2, 21, 2):
    print(i)
print("-----------------------------------")
# pares con %
print(">pares con % modulo<")
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
print("-----------------------------------")
# impares con %
print(">impares con % modulo<")
for i in range(1, 21):
    if i % 2 != 0:  # impar. si el (i) indice modulo  de 2 es diferente a 0 = impar
        print(i)

# list comprehension
# si quiero tener todos los pares o impares de una vez en una lista:
print("-----------------------------------")
print(">List comprehension<")  # ideal si quieres guardar los valores ademas de mostrarlos.

pares = [i for i in range(1, 20) if i % 2 == 0]
impares = [i for i in range(1, 20) if i % 2 != 0]  # yo lo leeria; iteracion por iteracion en el rango(tal) y luego lel metodo para
# obtener los pares o impares o lo que se requiera.

print(f"Pares {pares}")
print(f"Impares {impares}")

print("-----------------------------------")
# EXTRA!!
for i in range(1, 21):
    if i & 1 == 0:  # si el ultimo bit es 0, es par
        print(i)

# recomendacion:
# Quieres filtrar pares o impares mientras haces otras cosas? = usa % modulo
# Quieres una lista directa sin if? = usa range(inicio, fin, 2).
# Quieres guardar y trabajar con pares/impares? = usa lista por comprension
