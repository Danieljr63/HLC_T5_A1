numero_uno = int(input("Introduce un primer numero: "))
numero_dos = int(input("Introduce un segundo numero: "))
if numero_uno > numero_dos:
    print(numero_uno, "es mayor que", numero_dos)
elif numero_dos > numero_uno:
    print(numero_dos, "es mayor que", numero_uno)
elif numero_uno == numero_dos or numero_dos == numero_uno:
    print("los numeros son iguales")