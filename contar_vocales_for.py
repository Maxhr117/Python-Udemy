# contar vocales
frase = input("Escribe una frase: ")
vocales = "aeiou"
contador = 0

for letra in frase:
    if letra.lower() in vocales:
        contador += 1
print(f"La frase tiene {contador} vocales.")
