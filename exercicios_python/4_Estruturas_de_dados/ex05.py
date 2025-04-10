"""
5. Suponha o seguinte programa:
Exercícios – Estruturas de dados
    1# Alunos e suas notas representados através de dicionários
        alunos = [
            {
                "nome": "Alice",
                "nota": 8,
            },
            {
                "nome": "Bob",
                "nota": 7,
            },
            {
                "nome": "Carlos",
                "nota": 9,
            }
        ]
        Escreva uma programa que calcula a média das notas de todos os alunos.
"""
alunos = [
            {
                "nome": "Alice",
                "nota": 8,
            },
            {
                "nome": "Bob",
                "nota": 7,
            },
            {
                "nome": "Carlos",
                "nota": 9,
            }
        ]

soma = 0 
for nota in alunos:
    soma += nota['nota']
    print(f"nome: {nota['nome']} e {nota['nota']}")
media = soma // len(alunos)
print(f'A média das notas é {media}')