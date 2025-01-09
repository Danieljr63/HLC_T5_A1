def suma():
    numero_uno = int(input("Introduce un primer numero: "))
    numero_dos = int(input("Introduce un segundo numero: ")) 
    suma = numero_uno + numero_dos
    return suma

def mostrarSuma():
    resultado = suma()
    print("La suma es: ", resultado)
mostrarSuma()
