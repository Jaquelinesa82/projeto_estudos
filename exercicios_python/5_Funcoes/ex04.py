"""
4. Adapte a função maior_idade(pessoa) de forma que ela possa receber tanto uma
tupla quanto um dicionário. Dica: método type pode te ajudar.
"""
def maior_idade(pessoa):
    if isinstance(pessoa, tuple):  # Verifica se é uma tupla
        nome, idade = pessoa
    elif isinstance(pessoa, dict):  # Verifica se é um dicionário
        nome = pessoa.get("nome", "Desconhecido")
        idade = pessoa.get("idade", 0)
    else:
        print("Formato inválido.")
        return
    
    if idade >= 18:
        print(f"{nome} é maior de idade.")
    else:
        print(f"{nome} é menor de idade.")

# Exemplos de uso
p1 = ("Alice", 20)  # Tupla
p2 = {"nome": "Bob", "idade": 16}  # Dicionário
p3 = {"nome": "Carlos"}  # Dicionário sem idade
p4 = ["Daniel", 25]  # Lista (não suportada)

maior_idade(p1)  # Alice é maior de idade.
maior_idade(p2)  # Bob é menor de idade.
maior_idade(p3)  # Carlos é menor de idade (idade padrão 0).
maior_idade(p4)  # Formato inválido.
