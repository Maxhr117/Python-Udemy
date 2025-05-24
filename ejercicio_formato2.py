# Pide al usuario que ingrese su nombre, apellido paterno y apellido materno, todo en minúsculas (o desordenado).
# Une los valores en una sola cadena: Nombre ApellidoPaterno ApellidoMaterno.
# Muestra el nombre completo:
# Todo en mayúsculas
# Todo en minúsculas
# Con formato de título (cada palabra con la primera letra en mayúscula)

# esta es una segunda opcion

name = input('Ingrese nombre: ')
paternal_surname = input('Ingrese su apellido paterno: ')
maternal_surname = input('Ingrese su apellido materno: ')

full_name = f'{name} {paternal_surname} {maternal_surname}'

print('En minusculas', full_name.lower())
print('En mayusculas', full_name.upper())
print('En formato titulo', full_name.title())
