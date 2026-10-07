#Iram Jimenez NC = 0079
print("1. Python if")

print("Ejemplo 1:")
a = 33
b = 200
if b > a:
    print("b es mayor que a")

print("Ejemplo 2:")
x = 10
y = 10
if x == y:
    print("x e y son iguales")


print("2. Python IF ELIF")

print("Ejemplo 1:")
a = 33
b = 33
if b > a:
    print("b es mayor que a")
elif a == b:
    print("a y b son iguales")

print("Ejemplo 2:")
nota = 85
if nota >= 90:
    print("Excelente")
elif nota >= 80:
    print("Muy bueno")


print("3. Python IF ELSE")

print("Ejemplo 1:")
a = 200
b = 33
if b > a:
    print("b es mayor que a")
elif a == b:
    print("a y b son iguales")
else:
    print("a es mayor que b")

print("Ejemplo 2:")
edad = 16
if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")


print(" 4. Python ciclos for")

print("Ejemplo 1:")
animales = ["perro", "gato", "tigre"]
for x in animales:
    print(x)

print("Ejemplo 2:")
for x in ["león", "elefante", "jirafa", "cebra", "mono", "oso"]:
    print(x)


print("5. Python ciclos while")

print("Ejemplo 1:")
alimento_peces = 1
while alimento_peces < 6:
    print(alimento_peces)
    alimento_peces += 1

print("Ejemplo 2:")
patitos = 5
while patitos > 0:
    print(patitos)
    patitos -= 1