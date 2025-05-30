"""Calculo de area y perimetro de un rectangulo usando funciones"""


# Funcion para pedir un numero al usuario:
def pedir_medida(mensaje):
    return float(input(mensaje))


# Funcion para calcular el area:
def calcular_area(base, altura):
    return base * altura


# Funcion para calcular perimetro:
def calcular_perimetro(base, altura):
    return 2 * (base + altura)


# Funcion principal (el corazon del programa)
def main():
    print("CALCULADORA DE RECTANGULOS")

    # Entrada de datos
    base = pedir_medida("Ingresa la base del rectangulo: ")
    altura = pedir_medida("Ingresa la altura del rectangulo: ")

    # calculos
    area = calcular_area(base, altura)
    perimetro = calcular_perimetro(base, altura)

    # salida de resultados
    print("\nResultados: ")
    print(f"\nArea: {area:.2f}")
    print(f"\nPerimetro: {perimetro:.2f}")


# Ejecutamos el programa
main()
