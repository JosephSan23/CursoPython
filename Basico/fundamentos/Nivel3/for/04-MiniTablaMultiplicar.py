# El programa mostrara las tablas de multiplicar del 1 al 10
numero = int(input("Ingresa un numero: "))

for i in range(1, numero + 1):
    print(f"Tabla del {i}: ", end="")
    for j in range(1, 11):
        print(f" {i*j} ", end="")
    
    print(" ")