# Pepito tiene una alcancia donde va guardando dinero. Cada dia le pasa algo diferente que hace cambiar la cantidad.
# Usa operadores compuestos para actualizar su dinero.
# instrucciones:
# Pepito compienza con $50
# El lunes, gana $20.
# El martes, gasta $15.
# El miércoles, duplica lo que tiene.
# El jueves, compra un juguete de $40.
# El viernes, encuentra $10 tirado en la calle.
# Imprime cuánta plata tiene al final.

print('>Dinero de Pepito<')
print('Pepito comienza con $50 la semana')
dinero = 50
dinero += 20
dinero -= 15
dinero *= 2
dinero -= 40
dinero += 10
print(f'Pepito termina la semana con: $', dinero)

# Estás organizando una fiesta. Cada hora, pasa algo con las pizzas:
# 📝 Instrucciones:
# Empiezas con 8 pizzas.
# A la 1 PM, llegan 4 más.
# A las 2 PM, comen 5.
# A las 3 PM, duplicas las que quedan (un tío trae más).
# A las 4 PM, se comen el 25% (usa división).
# Imprime cuántas pizzas quedan.

print('***Fiesta de pizzas***')
print('se comienza con 8 pizzas')
pizzas = 8
pizzas += 4
pizzas -= 5
pizzas *= 2
pizzas /= 4

print(f"Al final quedaron: {pizzas} pizzas.")
