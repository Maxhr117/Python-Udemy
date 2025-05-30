# Supongamos que compramos varios articulos en el supermercado y queremos obtener
# el ticket de venta total incluyendo impuestos.
# -El sistema solicitará el precio de cada producto a comprar y el usuario
# debera indicar su precio. (valor de tipo con punto decimal)
# -El sistema debe realizar la suma de cada producto, calcular el
# impuesto y finalmente imprimir el total de la compra.
print('*** Generacion Ticket de venta ***')
coca_cola = float(input('Precio coca-cola: '))
leche = float(input('Precio leche: '))
azucar = float(input('Precio azucar: '))
huevos = float(input('Precio huevo: '))
tiene_descuento = str(input('>Tiene cupon de descuento? (si/no) <'))

# porcentaje de descuento
descuento_10 = 10 / 100  # 0.10
descuento_20 = 20 / 100  # 0.20

# Calculos basicos
total_items = (coca_cola + leche + azucar + huevos)
iva = 16 / 100  # 0.16
items_iva = (total_items * (16 / 100))
items_mas_iva = total_items + items_iva

# variables para el descuento
descuento_aplicado = 0
total_con_descuento = total_items

if tiene_descuento.lower() == 'si':
    cupon = input('Escriba su cupon de descuento: ')
    if cupon == 'DESC10':
        print('Cupon valido por 10% de descuento.')
        descuento_aplicado = total_items * descuento_10
        total_con_descuento = total_items - descuento_aplicado
    elif cupon == 'DESC20':
        print('Cupon valido por 20% de descuento.')
        descuento_aplicado = total_items * descuento_20
        total_con_descuento = total_items - descuento_aplicado
    else:
        print('Cupon NO valido.')
else:
    print('Sin descuento aplicado.')

# Calcular el IVA sobre el total con descuento
iva_final = total_con_descuento * iva
total_final = total_con_descuento + iva_final

# Mostrar resultados
print(f'Subtotal: {total_items:.2f}')
print('El precio de cada uno de sus articulos es: ', [coca_cola, leche, azucar, huevos])

if descuento_aplicado > 0:
    print(f'Descuento aplicado: ${descuento_aplicado:.2f}')
    print(f'Subtotal con descuento: ${total_con_descuento:.2f}')
else:
    print('Sin descuento')

print(f'IVA (16%){iva_final:.2f}')
print(f'Total de compra: ${total_final:.2f}')
