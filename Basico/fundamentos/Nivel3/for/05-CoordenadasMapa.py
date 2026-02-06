num_ancho = int(input("Ingresa un numero para el ancho: "))
num_alto = int(input("Ingresa un numero para el alto: "))

for i in range(1, num_ancho + 1):
    print(f"Fila {i}: ", end="")
    for j in range(1, num_alto + 1):
        print(f"({i},{j})", end="")
        
    print("")