nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
profissao = input("Digite sua profissão: ")


usuario = {
    "nome": nome,
    "idade": idade,
    "profissao": profissao
}

print("\n--- Registro Concluído ---")
print(f"Olá {usuario['nome']}, é um prazer ter um {usuario['profissao']} de {usuario['idade']} anos conosco!")
print(f"Dados brutos: {usuario}")