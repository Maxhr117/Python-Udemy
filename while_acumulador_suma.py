# Realizar la suma de los primeros 5 numeros utilizando un ciclo while:
# 1 + 2 + 3 + 4 + 5 -> 15

numero_maximo = 5
suma = 0
i = 1
while i <= numero_maximo:
    # Imprimir lo que se va a sumar
    print(f"(suma + i) -> {suma} + {i}")
    # Ejecuta  la suma iterativa o acumulada
    suma += i
    i += 1
    # Imprimir el resultado parcial
    print(f"Suma parcial acumulada: {suma}")
print(f"La suma acumulada es: {suma}")
