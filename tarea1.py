
puntuacion = int(input("Introduce tu puntuación (0-100): "))

if puntuacion >= 90:
    nota = "A"
elif puntuacion >= 80:
    nota = "B"
elif puntuacion >= 70:
    nota = "C"
elif puntuacion >= 60:
    nota = "D"
else:
    nota = "F"

print(f"Tu calificación es: {nota}")