base = int(input("Introduce un numero que sea la base: "))
altura = int(input("Introduce un numero que sea la altura: "))
precio = int(input("Introduce el precio por metro cuadrado: "))

area_triangulo = (base * altura) / 2

costo = area_triangulo * precio
print("base =", base, "altura =", altura, "precio =", precio)
print(area_triangulo, "metros cuadrados", "Costo total =", costo, "unidades")