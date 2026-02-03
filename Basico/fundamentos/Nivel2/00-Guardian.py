# "El Guardián de la Discoteca"

nombre = input("Ingrese su nombre: ")
# Pide la edad y el dinero que tiene el usuario:
edad = int(input("¿Que edad tienes?: "))
dinero = int(input("¿Cuanto dinero tienes?: "))

# Logica de la decision:
if edad >= 18 and dinero >= 50:
    print(f"¡Bienvenido al VIP {nombre}!")
    if edad >= 18 and dinero >= 100:
        print("Ademas tienes un trago gratis de cortesia")
elif edad >= 18 and dinero < 50:
    print("Puedes pasar, pero solo a la zona general.")
else:
    print("Lo siento eres menor de edad")
