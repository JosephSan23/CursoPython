import random 
secreto = random.randint(1,20)
intentos = 1
print("Bienvenido, debes adivinar que numero eligio el programa, tienes 5 intentos")


while intentos <= 5:
    respuesta = int(input(f"Intento Numero {intentos}/5 Ingresa un numero: "))
    if respuesta == secreto:
        print(f"Adivinaste el numero: {secreto} al intento N{intentos}")
        break
    elif respuesta > secreto:
        print(f"El numero secreto es menor que {respuesta}")
    else:
        print(f"El numero secreto es mayor que {respuesta}")
    intentos += 1
    
    if intentos > 5:
        print(f"El numero era {secreto}, suerte para la proxima")
        
    