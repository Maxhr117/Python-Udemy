# ejercicio: sumar los numeros pares del 1 al 100
# objetivo:
# Recorrer los numeros del 1 al 100
# Detectar cuales son pares.
# sumar todos esos pares.
# impirmir el resultado final.

print("> 1: Usando % para contar el numero de pares dentro del rango<")
total_de_pares = 0
for i in range(1, 101):
    if i % 2 == 0:
        total_de_pares += 1
print(f"El total de pares entre 1 al 100 es: {total_de_pares} ")

print("-----------------------------------")

print("> 2: Usando range(2, 101, 2) (mas directo)")
# suma_pares = 0
pares = 0
for i in range(2, 101, 2):
    pares += i
print(f"La suma de los pares del 1 al 100 es: {pares}")
