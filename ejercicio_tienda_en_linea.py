# Tienda en linea
"""
Crear un sistema que ofrezca descuentos dependiendo del monto de la compra,
  si es miembro de la tienda.
Se deben revisar las siguientes condicioneS:
1- Si ha comprado más de $1,000 Y es miembro -> Descuento de 10%
2- Si solo es miembro de la tienda -> Descuento del 5%
3- Si no es miembro ni compro más de $1,000 -> Descuento del 0%.
"""
# compra minima $1,000
print('***Tienda en linea***')
compra = float(input('>Ingrese el monto de su compra: '))
miembro = str(input('tienes membresia?: (si/no)'))

if compra >= 1000 and miembro.lower() == 'si':
    print('Tienes un descuento de 10% ')
    descuento = (compra * 10 / 100)
    print(f"{descuento:.2f}")
    precio_final = compra - descuento
    print(f'Tu precio final a pagar es: {precio_final:.2f}')
elif compra < 1000 and miembro.lower() == 'si':
    print('Tienes un descuento de 5% ')
    descuento = (compra * 5 / 100)
    print(f"{descuento:.2f}")
    precio_final = compra - descuento
    print(f'Tu precio final a pagar es: {precio_final:.2f}')
else:
    print(f'No obtienes ningun descuento. \n>Total a pagar: {compra:.2f}')
