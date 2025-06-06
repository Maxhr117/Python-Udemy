# Lista
nombres = ["Jhon", "Linda", "Fredd", "Kelly"]
print("El tipo de nombres es", type(nombres))
for nombre in nombres:
    print(f"Buenos dias {nombre}")
print("------------------------------------------")
# Tuple
nombres = ("Jhon", "Linda", "Fredd", "Kelly")
print("El tipo de nombre es", type(nombres))
for nombre in nombres:
    print(f"Buenos dias {nombre}")
print("------------------------------------------")
# Set
nombres = {"Jhon", "Linda", "Fredd", "Kelly"}
print("El tipo de nombre es", type(nombres))
for nombre in nombres:
    print(f"Buenos dias {nombre}")
# Diccionario
print("------------------------------------------")
nombres = {"Jhon": 1, "Linda": 2, "Fredd": 3, "Kelly": 4}
print("El tipo de nombre es", type(nombres))
for nombre in nombres:
    print(f"Buenos dias {nombre}")
print("------------------------------------------")
# range
for i in range(3, 11, 2):
    print(i)
