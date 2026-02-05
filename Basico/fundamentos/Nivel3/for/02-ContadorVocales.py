# Escribe una frase
frase = input("Ingresa una frase: ")
contar_vocales = 0

for letra in frase:
    if letra == " ":
        continue
    
    if letra in "aeiou":
        contar_vocales += 1
    
print(f"Hay {contar_vocales} vocales en la frase")