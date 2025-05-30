def calcular_total_compra():
    """
    Solicita el precio de varios productos, calcula el subtotal,
    aplica el IVA (16% en México) y muestra el total de la compra.
    """
    productos = []
    while True:
        try:
            precio_str = input("Ingresa el precio del producto (o 'fin' para terminar): ")
            if precio_str.lower() == 'fin':
                break
            precio = float(precio_str)
            if precio < 0:
                print("El precio no puede ser negativo. Inténtalo de nuevo.")
                continue
            productos.append(precio)
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número o 'fin'.")

    if not productos:
        print("No se ingresaron productos. El total de la compra es $0.00.")
        return

    subtotal = sum(productos)
    IVA_RATE = 0.16  # 16% de IVA en México
    impuesto = subtotal * IVA_RATE
    total_compra = subtotal + impuesto

    print("\n--- Ticket de Venta ---")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"IVA (16%): ${impuesto:.2f}")
    print(f"Total a pagar: ${total_compra:.2f}")
    print("----------------------")


# Llamar a la función para ejecutar el programa
if __name__ == "__main__":
    print("¡Bienvenido al sistema de cálculo de ticket de venta!")
    print("Por favor, ingresa el precio de cada producto.")
    print("Cuando hayas terminado, escribe 'fin' y presiona Enter.")
    calcular_total_compra()
