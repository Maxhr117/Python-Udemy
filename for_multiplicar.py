print("#Imprimir la tabla del 5 -> Usar un for para imprimir la tabla del 5, del 1al 10.")

for i in range(1, 11):
    resultado = 5 * i  # 5 es el numero que se proporciono para hacer la multiplicacion
    print(f"5 x {i} = {resultado}")
print("------------------------------------------")

print("# 2 funcion para cualquier numero\nnumero proporcionado para la funcion: 7")
def tabla_del(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

tabla_del(7)

print("------------------------------------------")
print("# 3 Crear una funcion que reciba dos numeros (a y b) y sume todos losmultiplos de 3 entre ellos (inclusive si a o b son multiplos de 3)\nnumeros proporcionados para la funcion: (3, 10)")

def sumar_multiplos_de_3(a, b):
    if a > b:
        a, b = b, a  # Nos aseguramos de ir de menor a mayor
    suma = 0
    for i in range(a, b + 1):
        if i % 3 == 0:
            suma += i
    return suma
print(sumar_multiplos_de_3(3, 10))