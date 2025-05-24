# Ejercicio: formatear nombre completo del usuario
# 1- pide al usuario que ingrese su numero, apellido paterno y apellido materno, todo en desordenado.
# 2- Une los valores en una sola cadena: Nombre Apellido_paterno Apellido_Materno.
# 3- Muestra el nombre completo:
# todo en mayusculas
# todo en minusculas
# con formato de titulo

n0mbre = input('Ingrese su nombre ')
apellido_Paterno = input('Ingrese su apellido paterno ')
apellido_Materno = input('Ingrese su apellido materno ')

print(n0mbre)
print(apellido_Paterno)
print(apellido_Materno)

print()

nombre_minusculas = n0mbre.lower()
apellido_p_minusculas = apellido_Paterno.lower()
apellido_m_minusculas = apellido_Materno.lower()
nombre_mayusculas = n0mbre.upper()
apellido_p_mayusculas = apellido_Paterno.upper()
apellido_m_mayusculas = apellido_Materno.upper()
nombre_title = n0mbre.title()
apellido_p_title = apellido_Paterno.title()
apellido_m_title = apellido_Materno.title()
print(f'Nombre completo en minusculas: {nombre_minusculas} {apellido_p_minusculas} {apellido_m_minusculas}.')
print(f'Nombre completo en mayusculas: {nombre_mayusculas} {apellido_p_mayusculas} {apellido_m_mayusculas}.')
print(f'Nombre completo en formato titulo: {nombre_title} {apellido_p_title} {apellido_m_title}.')
