# Calculador de vida
# Realizar un programa que haga lo siguiente:

# Pide al usuario su nombre y guardalo en una variable:
nombre = input("Ingrese su nombre: ")

# Pida su edad (Convertirlo en entero):
edad = int(input("Ingrese su edad: "))

# Pida su peso:
peso = float(input("Ingrese su peso: "))

dias_vivos = edad * 365

print(f"Hola {nombre}, segun tu {edad} años, has vivido aproximadamente {dias_vivos} dias y pesas {peso} kg")