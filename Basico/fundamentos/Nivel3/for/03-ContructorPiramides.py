numero = int(input("Ingresa un numero entero: "))

for i in range(1, numero + 1):
    for j in range(i):
        print("*", end="")
    print("")
    
