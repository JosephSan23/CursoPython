# pide al usuario un numero positivo
numero = int(input("Ingresa un numero positivo: "))
es_primo = True

for i in range(2, numero):
    if numero % i == 0:
        es_primo = False
        break
      
if es_primo == False:
    print(f"El numero: {numero} no es primo")
else:
    print(f"El numero: {numero} es primo")