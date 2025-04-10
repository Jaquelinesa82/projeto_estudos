"""
4. Suponha o seguinte programa:
    # Alunos e suas respectivas notas
    alunos = [
        ("Alice", 8),
        ("Bob", 7),
        ("Carlos", 9),
    ]
    Escreva uma programa que calcula a média das notas de todos os alunos. 
"""
alunos = [
        ("Alice", 8),
        ("Bob", 7),
        ("Carlos", 9),
    ]

soma = 0
for nome, nota in alunos:
    soma += nota

media = soma // len(alunos)
print(media)