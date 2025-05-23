# Dado un producto de una tienda en linea, generar 3 variables para almacenar:
# 1. El nombre del producto
# 2. El precio del producto
# 3. La cantidad disponible
# - Finalmente mandar a imprimir el valor de cada variable.

item1 = 'Leche'
price_item1 = 20
cant = 23

print('*** Informacion del Producto ***')
print(f'Nombre del producto: {item1}')
print(f'Precio del producto: ${price_item1}')
print(f'Cantidad del producto: {cant} piezas')

# cambios en el precio o cantidad inicial
price_item1 = 22.50
cant = 10
print()
print('*** Informacion del Producto actualizada ***')
print(f'Nombre del producto: {item1}')
print(f'Precio del producto: ${price_item1}')
print(f'Cantidad del producto: {cant} piezas')
