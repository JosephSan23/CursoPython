# Entrada de datos
nota = float(input("Introduce tu nota (0-10): "))
edad = int(input("Introduce tu edad: "))

# Primer nivel: ¿Aprobó?
if nota >= 6:
    print("¡Felicidades! Has aprobado.")
    
    # Segundo nivel (Anidado): ¿Tiene excelencia?
    if nota >= 9:
        print("Tienes un promedio excelente.")
        
        # Tercer nivel (Anidado): ¿Aplica a beca por edad?
        if edad < 18:
            print("Calificas para la Beca de Jóvenes Talentos.")
        else:
            print("Calificas para la Beca de Excelencia Universitaria.")
    else:
        print("Sigue esforzándote para alcanzar la excelencia.")

else:
    print("Lo siento, no has aprobado esta vez.")
    
    # Segundo nivel (Anidado): ¿Cerca de aprobar?
    if nota >= 5:
        print("Estás muy cerca, puedes solicitar un examen de recuperación.")
    else:
        print("Debes recursar la materia.")