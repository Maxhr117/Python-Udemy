# 1 Suma los primeros 10 numeros naturales

suma = 0  # suma comienza con valor 0
for i in range(1, 11):  # Desde la el numero 1 hasta el 10.
    suma += i
print(f"La suma de los primeros 10 numeros es: {suma} ")

print("------------------------------------------")

# 2 Suma de numeros pares del 1 al 100 usando for.
sum4 = 0  # suma comienza con valor 0
for i in range(1, 101):
    if i % 2 == 0:
        sum4 += i
print(sum4)

print("------------------------------------------")

# 3 suma los digitos de un numero
# Dado un numero como 12345, usar un for para sumar sus digitos.
numero = 12345  # En este caso nosotros brindamos el numero
texto = str(numero)  # ahora convertimos el numero a un string y podemos recorrerlo letra por letra

suma = 0  # suma comienza con valor 0
for digito in texto:  # aqui recorremos el numero ahora que es string
    suma += int(digito)  # aqui volvemos a convertir cada "letra" en numero(int) para poder hacer la suma
print(f"La suma de los digitos es: {suma}")

print("------------------------------------------")
