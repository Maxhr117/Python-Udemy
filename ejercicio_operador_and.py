# ejercicio 1 = El doctor esta creando una formula para un suero especial que solo se activa si ambos
# ingredientes estan listos y la temperatuar es la correcta.
# instrucciones:
# ingrediente A esta listo: True
# ingrediente B esta listo: Falste
# temperatura atual: 100
# temperatura ideal: entre 95 y 105
# Tu tarea es escribir un condicional que solo imprima "Formula activada!" si:
# ambos ingredientes estan listos
# y la temperatura esta dentro del rango ideal

ingredienteA = True
ingredienteB = True
temperatura = 100
print("01---Ingredientes para formula---")
if ingredienteA and ingredienteB and temperatura >= 95 <= 105:
    print('Formula activada')
else:
    print('Los ingredientes NO estan listos')
print()

# ejercicio 2 = Un valiente caballero quiere entrar al castillo, pero el guardia magico solo lo dejara pasar si cumple
# ambas condiciones:
# >Tiene una espada(tiene_espada = True)
# >Tiene una contrasena secreta correcta ( clave_ingresada == 'dracarys')
# ---Escribir un programa qe imprima:
# "Bienvenido, heroe!" si ambas condiciones se cumplen.
# "Alto ahi! no puedes entrar al castillo." en cualquier otro caso.
print("02---Entrada a castillo---")
tiene_espada = True
clave_ingresada = "dRacARys"
if tiene_espada and clave_ingresada.lower() == "dracarys":
    print("Bienvenido, Heroe!")
else:
    print("Alto ahi! NO puedes entrar al castillo !")

# ejercicio 3 = Mateo quiere salir a volar su comenta, pero solo lo hara si:
# NO esta lloviendo (llueve = False)
# Y el viento esta entre 15 y 30 km/h
# Decirle a Mateo si puede salir o no:
print()
print("03---Volar cometa---")
llueve = False
viento = 20
if llueve and viento >= 15 <= 30:
    print('Mateo puedes salir a votar tu comenta !')
else:
    print('Lo siento Mateo, NO puedes salir por ahora.')

# ejercicio 4 = Para entrar a la torre de sabiduria, el mago solo permite el paso a quien:
# Sea mayor o igual a 20 anos.
# Y tenga un nivel de magia mayor a 70.
# Verifica si un personaje puede entrar o no.
print()
print("04---Torre sabiduria---")
edad = int(input('>Ingresa tu edad guerrero<: '))
nivel = int(input('>Ahora ingresa tu nivel actual<: '))
if edad >= 20 and nivel >= 70:
    print('Puedes entrar a la torre guerrero !')
else:
    print('NO cumples con los requisitos para entrar a la torre.')

# ejercicio 5 = Estas programando un sistema de acceso a un laboratorio secreto de alta seguridad.
# Para que una persona tenga acceso, debe cumplir TODAS ESTAS CONDICIONES.
# >Tener una EDAD ENTRE 21 Y 65 ANOS
# >Haber ingresado la CLAVE CORRECTA("clave123", sin importar mayusuculas o minusculas)
# >Tener PERMISO ESPECIAL ACTIVADO(permiso = True)
# Escribir un programa que imprima:
# ---"Acceso concedido✅" si cumple con TODO
# ---"Acceso denegado❌" si CUALQUIER CONDICION FALLA
print()
print("05---Acceso laboratorio---")
edad = int(input(">Ingrese su edad<: "))
clave_correcta = input(">Ahora ingrese la clave<: ")
permiso = True
if edad >= 21 <= 65 and clave_correcta.lower() == "clave123" and permiso:
    print("Acceso concedido✅")
else:
    print("Acceso denegado❌")

# ejercicio 6 = Una universidad magica da becas solo a estudiantes que cumplan TODOS los siguientes requisitos:
# >Tener promedio MAYOR O IGUAL a 8
# >haber asistido AL MENOS al 90% de las clases
# >Y tener ENTRE 17 Y 25 anos.
# ---Decir si el estudiante recibe la beca o no.
print()
print("06---Beca universidad---")
promedio = 10
asistencia = 95  # en porcentaje
edad = 24
if promedio >= 8 and asistencia >= 90 and edad >= 15 <= 25:
    print("Felicidades, recibes la beca!")
else:
    print("Lo siento, NO calificas para la beca!")

# ejercicio 7 = Sistema Descuentos VIP
# Una tienda de supermercado ofrece un descuento especial a clientes que compren 10 o mas articulos por dia Y ademas
# sean miembros de la tienda.
# El sistema debe solicitar al cliente que indique cuantos articulos ha comprado en el dia y preguntarle si
# cuenta con la membresia de la tienda.
# En caso de haber comprado 10 o mas productos y ser miembro de la tienda entonces tendra acceso al descuento VIP.

print()
print("07---Sistema de Descuentos VIP---")
productos_para_descuento = 10
cantidad_productos = int(input(">Ingrese la cantidad de productos que esta llevando<: "))
miembro = input(">Es usted miembro de la tienda? (si/no)<: ")
if cantidad_productos >= 10 and miembro.lower() == 'si':
    print('>ERES ACREEDOR AL DESCUENTO VIP<')
else:
    print('>LO SIENTO, NO APLICAS AL DESCUENTO VIP<')
