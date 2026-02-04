# Escribe un programa que permita ingresar notas una por una hasta que el usuario decida parar.
contador = 0
suma = 0
print("Este es un calculador de notas vas a colocar notas y cuando quieras parar pones -1")

while True:
    notas = float(input(f"Ingresa la nota numero {contador + 1}: "))
    if notas == -1:
        break
    suma += notas
    contador += 1
    print(f"Suma acumulada: {suma}")
    
    if contador > 0:
        promedio = suma / contador
        print("RESULTADOS")
        print(f"Notas ingresadas: {contador}")
        print(f"Suma total: {suma}")
        print(f"Promedio: {promedio}")
    else:
        print(f"No se ingresaron notas para calcular")
    
    
    