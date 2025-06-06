# Sistema de Envios
"""Crea un programa paradeterminar el costo de envio de un paquete segun el destino
(nacional o internacional) y el peso del paquete.
>Costo Tarifas :
-Nacional = 10 x kilo
-Internacional = 20 x kilo
El programa debe solicitar 2 valores:
    1 >  Destino(Nacional o Internacional)
    2> Peso(kilogrmos) del paquete.
Al final debe imprimir el costo de envio del paquete."""

peso_del_paquete = float(input('Ingresar peso del paquete en kg: '))
destino = str(input('Destino? (Nacional/Internacional)'))
tarifa_nacional = 10 * peso_del_paquete
tarifa_internacional = 20 * peso_del_paquete
costo_envio = ''

if destino.lower() == 'nacional':
    costo_envio = tarifa_nacional
elif destino.lower() == 'internacional':
    costo_envio = tarifa_internacional
print(f'> El costo de envio por tu paquete es: ${costo_envio:.2f}')
