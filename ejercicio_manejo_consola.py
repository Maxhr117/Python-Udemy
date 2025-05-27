# Crea un prorgama para solicitar al usuario que proporcione por consola la siguiente informacion.
# -Nombre
# -Edad(como un valor de tipo entero)
# -Pais
# >Mandar a imprimir utilizando fstring()

nombre = (input('Ingresa tu nommbre: '))
edad = int(input('Ingresa tu edad: '))
pais = (input('Ingresa tu pais: '))

print(f'Tu nombre es: {nombre}, tu edad:{edad}, y tu pais de origen es{pais}')
print(type(nombre))
print(type(edad))
print(type(pais))
