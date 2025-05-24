# cadena[inicio:fin]
# inicio: posicion desde donde comienza(incluye ese indice)
# fin: posicion donde termina (sin incluir ese indice)
# si omites alguno, toma el inicio o el final por defecto.

# ejemplo
ejemplo = 'Python'
print(ejemplo[0:4])  # Resultado (indices 0, 1, 2, 3)
# otras formas utiles de slicing:
print(ejemplo[2:])  # thon desde indice 2 hasta el final
print(ejemplo[:3])  # pyt desde inicio hasta el indice 2
print(ejemplo[-1])  # n ultimo caracter
print(ejemplo[-3:])  # hon ultimos 3 caracteres
print(ejemplo[::2])  # pto cada 2 caracteres
print(ejemplo[::-1])  # nohtyp cadena invertida

# importante: los indices empiezan desde 0. Puedes usar indices negativos para contar desde el final.
