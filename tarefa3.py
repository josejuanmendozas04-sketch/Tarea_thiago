
frase = input("Digite uma frase: ")

palavras = frase.split()
quantidade = len(palavras)

print(f"\nA frase em maiúsculas: {frase.upper()}")
print(f"A frase contém {quantidade} palavras.")