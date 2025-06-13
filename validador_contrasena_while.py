# El usuario tiene que ingresar la contrasena correcta para continuar
# Tiene 3 intentos antes de que se bloquee el acceso
"""
Primero debemos analizar como sera el flujo del programa, 
en este caso debemos controlar primero el numero de intentos 
que se daran antes de bloquear el acceso. Dentro de ese ciclo(loop)
es en donde daremos las instrucciones de como queremos que el usuario
introdusca los datos y cuantas veces.

"""
contrasena_correcta = "Python123"
intentos = 0
maximo_de_intentos = 3

while intentos < maximo_de_intentos: #aqui delimitamos cuantas veces va a recorrer esta condicion.
    entrada = input("Introduce la contrasena: ")
    if entrada == contrasena_correcta:
        print("Acceso consedido.")
        break # Con esto detenemos que siga repitiendose el ciclo directamente
    else:
        print("Contrasena incorrecta.")
        intentos += 1
if intentos == maximo_de_intentos:
    print("Acceso bloqueado. Demasiados intentos.")