# ejercicio_4.py
numeros = [12, 5, 8, 3, 20, 15, 7, 10]
pares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)

print(f"Lista original: {numeros}")
print(f"Apenas os números pares: {pares}")