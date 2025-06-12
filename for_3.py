# Para cada animal en la lista animales, impirmir un saludo.
animales = ["perro", "gato", "pato"]
for animal in animales:
    print(f"Hola {animal}")
# range() genera una secuencia de numeros.
for i in range(5):
    print(f"iteracion numero {i}")
# variantes utiles para range():
# range(inicio, fin) -> Empieza desde inicio, termina antes de fin.
# range(inicio, fin, paso) ->Ademas, puedes definir el salto.
for i in range(2, 11, 2):  # Esto imprime numeros pares del 2 al 10.
    print(i)

for i in range(1, 11, 3):  # aqui iteramos cada 3 numeros
    print(i)

# cuando utilizar for?
# usarlo cuando: sabes cuantas veces quieres repetir algo.
# cuando quieres recorrer elementos de una lista, texto o rango.
