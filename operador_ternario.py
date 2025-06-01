# Ejemplo del operador ternario en Python
# sintaxis:
# Valor_si_verdadero if condicion else valor_si_falso

edad = 20
mensaje = 'Mayor de edad' if edad >= 18 else "Menor de edad"
print(mensaje)  # Imprime: Mayor de edad


# Otro ejemplo con funcion
def evaluar_nota(nota):
    return "Aprobado" if nota >= 60 else "Reprobado"


print(evaluar_nota(75))  # Imprime: Aprobado
print(evaluar_nota(45))  # Imprime: Reprobado
