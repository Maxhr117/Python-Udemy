# El operador and en Python compara dos condiciones y **solo devuelve True si ambas son True.
# Es como si dijera:
# “Si esto es cierto y aquello también es cierto, entonces sí. Si no, olvídate.”
# OJO True y False siempre se indican con la primera letra Mayuscula para tomarlo como operador.

# Tabla de la verdad(and)
# | Condición A | Condición B | A and B |
# | ----------- | ----------- | ------- |
# | True        | True        | True    |
# | True        | False       | False   |
# | False       | True        | False   |
# | False       | False       | False   |
# Solo hay una manera de obtener True y es que ambas sean verdaderas!
# ej.
tengo_hambre = True
hay_postre = True
if tengo_hambre and hay_postre:
    print('Hora del postre, a comer !')
else:
    print('No hay postre ahora !')
# ej2.
# Puedes entrar a una montana rusa?
edad = 10
altura = 1.55
if edad >= 18 and altura >= 1.55:
    print('Adelante! puedes ingresar !')
else:
    print('Lo siento, NO puedes ingresar !')
