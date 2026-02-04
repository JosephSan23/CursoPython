# Crea un programa que simule un cajero
# Crea una variable saldo con valor de 1000
saldo = 1000

# Usa un bucle while para que el programa siempre muestre este menu
while True:
    print("1. Consultar saldo")
    print("2. Retirar Dinero")
    print("3. Salir")
    opciones = int(input("Elige una de las opciones: "))
    
    if opciones == 1:
        print(f"Tu saldo actual es: ", saldo)
    elif opciones == 2:
        print("Retirar Dinero")
        monto_retirar = int(input("Cuanto dinero deseas retirar: "))
        if monto_retirar > saldo:
            print("Fondos insuficientes")
        else:
            saldo -= monto_retirar
            print(f"Retiraste {monto_retirar} USD")
            print(f"Tu saldo actual es de: {saldo}")
    elif opciones == 3:
        print("Gracias por usar nuestro cajero, Adios")
        break
    else:
        print("Opcion no valida, intenta de nuevo")
        