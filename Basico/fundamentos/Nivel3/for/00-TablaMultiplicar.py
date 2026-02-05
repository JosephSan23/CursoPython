# Pide al usuario un número (ej. 7).
numero = int(input("Ingresa un numero: "))

# Usa un for y la función range() para mostrar la tabla de multiplicar del 1 al 10.
for i in range(1, 11):
    multiplicacion = numero * i
    if multiplicacion == 0:
        print(f"Toda multiplicacion x 0 da 0")
    if multiplicacion % 2 == 0:
        print(f"{multiplicacion}: El numero es par")
    else:
        print(f"{multiplicacion}: El numero es impar")