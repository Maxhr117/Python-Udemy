# -Crear un programa para solicitar algunos valores importantes para una receta de cocina.
# Los valores que debe introducir el usuario son:
# Nombre de la receta
# Ingredientes en una sola cadena separandolos por una coma(,)
# Tiempo de preparacion(en minutos) en tipo entero
# Dificultd ('Facil, Media, Alta')
# Mandar a imprimir la receta
print('*** Creemos una receta deliciosa ***')
print('Por favor introduce los siguientes datos: ')
nombre = input('Nombre de la receta: ')
ingredientes = input('Dame los ingredientes para la receta separados por una coma (,): ')
tiempo = (int(input('Cuanto es el tiempo estimado de preparacion(en minutos)?: ')))
dificultad = input('Que dificultad tiene esta receta?: ')
print('---------------------')
print(f'Nombre de la siguiente receta: {nombre}.')
print(f'Los ingredientes para la receta son: {ingredientes}.')
print(f'El tiempo estimado de preparacion son {tiempo} minutos.')
print(f'La dificultad de esta receta es {dificultad}.')
