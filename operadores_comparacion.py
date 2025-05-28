# ¿Qué son los operadores de comparación?
# Imagina que tienes dos cosas (números, por ejemplo) y quieres compararlas.
# Los operadores de comparación son los que preguntan cosas como:
# “¿Son iguales?”,
# “¿Uno es más grande?”,
# “¿Este es menor o igual que el otro?”
# Y luego te responden muy honestamente con un True (verdadero) o False (falso).

# Operador	¿Qué pregunta hace?	               Ejemplo	        Resultado
#   ==	    ¿Son iguales?	                    5 == 5	        True
#   !=	    ¿Son diferentes?	                5 != 3	        True
#   >	    ¿Es mayor que...?	                7 > 2	        True
#   <	    ¿Es menor que...?	                3 < 10	        True
#   >=	    ¿Es mayor o igual que...?	        6 >= 6	        True
#   <=	    ¿Es menor o igual que...?	        4 <= 5	        True

# ejercicio 1
# Juan y Lucía están en clase y compiten por ver quién tiene más lápices.
# Instrucciones:
# Juan tiene 8 lápices.
# Lucía tiene 10 lápices.
# Usa operadores de comparación para responder:
# ¿Tienen la misma cantidad?
# ¿Juan tiene más que Lucía?
# ¿Lucía tiene 8 o más?

lapices_juan = 8
lapices_lucia = 10
print(f'>---Juan tiene {lapices_juan} lapices y Lucia tiene {lapices_lucia} lapices.---<')
print(f'Lucia y Juan tienen la misma cantidad de lapices?: {lapices_lucia == lapices_juan}')
print(f'Juan tiene mas lapices que Lucia?: {lapices_juan > lapices_lucia}')
print(f'Lucia tiene 8 o mas lapices? {lapices_lucia > 8}')
print()

# ejercicio 2
# Estás en una fiesta. Hay 15 cupcakes y 12 invitados hambrientos.
# Preguntas:
# ¿Hay suficientes cupcakes para que cada invitado tenga al menos uno?
# ¿Hay más cupcakes que invitados?
# ¿Hay exactamente 15 invitados?

cupcakes = 15
invitados = 12
print(f'>---En una fiesta hay {cupcakes} cupcakes y {invitados} invitados.---<')
print(f'Hay suficientes cupcakes para que cada invitado tenga al menos uno? {cupcakes == invitados}')
print(f'Hay mas cupcakes que invitados? {cupcakes > invitados}')
print(f'Hay exactamente 15 invitados? {invitados == 15}')
print()

# ejercicio 3
# Una tortuga, una liebre y un caracol hacen una carrera.
# La tortuga avanza 12 metros.
# La liebre 18 metros.
# El caracol… apenas 3 metros.
# Preguntas:
# ¿La liebre le ganó a la tortuga?
# ¿El caracol quedó en último lugar?
# ¿La tortuga avanzó más que 10 metros?
print(">---Una tortuga, una liebre y u caracol hace una carrera.---<")
tortuga = 12
liebre = 18
caracol = 3
print(f'La liebre le gano a la tortuga?: {liebre > tortuga}')
print(f'El caracol quedo en ultimo lugar?: {caracol < 12}')
print(f'La tortuga avanzo mas que 10 metros?: {tortuga > 10}')
