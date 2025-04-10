"""
1. Escreva um programa que receba um número inteiro n e imprima a soma de todos
os números de 1 até n (inclusive n ).
"""

num = int(input('Digite um número: '))
soma = 0
i = 1
# total = sum(range(1, num + 1)) # usando a função SUM
while i <= num:
    soma += i
    i += 1
print(f'A soma  de todos os números de 1 até {num} e de:{soma}')
