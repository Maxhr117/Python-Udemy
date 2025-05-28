# Operadores de asignacion compuestos
print("****Operadores de asignacion compuestos****")
a, b = 10, 15
print(f'Valor incial a: {a}, Valor incial b: {b}')

# Operador compuesto de suma +=
a += b  # a = a + b
print(f'Operador a += b es: {a}')
# Ejemplos
# Operador	¿Qué hace?	            Ejemplo antes	  Ejemplo después
#  +=	    Suma y asigna	            x += 3	        x = x + 3
#  -=	    Resta y asigna	            x -= 2	        x = x - 2
#  *=	    Multiplica y asigna	        x *= 4	        x = x * 4
#  /=	    Divide y asigna	            x /= 2	        x = x / 2
#  //=	    División entera y asigna	x //= 3	        x = x // 3
#  %=	    Módulo y asigna	            x %= 2	        x = x % 2
#  **=	    Potencia y asigna	        x **= 2	        x = x ** 2

juguetes = 10  # tienes 10 juguetes
juguetes += 5  # Tu mama te dio 5 juguetes mas
juguetes -= 2  # Le diste 2 juguetes a tu hermano
juguetes *= 2  # multiplicaste tu cantidad de juguetes * 2 magicamente
juguetes //= 3  # dividiste el total de tus juguetes /3 para tu hermano, tu primo y tu

print(f'juguetes en total: {juguetes}')
