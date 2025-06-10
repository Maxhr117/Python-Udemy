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
nombres = {"Jhon": 117, "Linda": 58, "Fred": 104, "Kelly": 87}
print("El tipo de nombre es", type(nombres))
for i in nombres:
    print(f"Buenos dias  {i} -> {nombres[i]}")
print("------------------------------------------")
# range
for i in range(1, 20, 2):
    print(i)
print("------------------------------------------")
