# Operador or
# El operador or se usa cuando quieres que AL MENOS UNA de las varias condiciones sea VERDADERA.
# No hace falta que todo sea perfecto, con que UNA COSA FUNCIONE, YA ALCANZA.
# esto es verdad o aquello es verdad? con que UNA lo sea, devuelve True.
# Tabla de la verdad de or:
# | Condición A | Condición B | A or B |
# | ----------- | ----------- | ------ |
# | True        | True        | True   |
# | True        | False       | True   |
# | False       | True        | True   |
# | False       | False       | False  |
# solamente devuelve False si TODO ES FALSO.
# ejemplo:
hay_pizza = True
hay_pozole = False
print('hay algo de cenar?')
if hay_pizza or hay_pozole:
    print('Si, hay algo de cenar.')
else:
    print('Negativo, no hay cena.')
# or dice: Si hay varias formas de lograr un mismo objetivo.
# Muy util cuando HAY VARIAS FORMAS DE LOGRAR UN MISMO OBJETIVO.
# Se usa cuando NO TODAS LAS CONDICIONES SON OBLIGATORIAS, solo con que UNA  se cumpla, devuelve True.
