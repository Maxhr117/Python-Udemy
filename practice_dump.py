#   i es un numero par?True/False
i = 10
print(i % 2 == 0)

i = 15
print(i % 2 == 0)
print("-----------------------------")
# i es un numero impar?
i = 8
print(i % 3 == 0)

i = 15
print(i % 3 == 0)
print("-----------------------------")

# En un bucle se utiliza asi:
for i in range(1, 11):
    if i % 2 == 0:
        print(i, "es par.")
    elif i % 3 == 0:
        print(i, "es impar.")

print("-----------------------------")

contador = 0
suma = 0
while contador < 5:
    contador += 1
    suma += contador

    print(f"contando: {suma}")
