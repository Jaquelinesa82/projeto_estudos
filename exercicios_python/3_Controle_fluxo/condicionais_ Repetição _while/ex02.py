"""
2. Escreva um programa que receba um número inteiro n e imprima todos os
números pares de 1 até n (inclusive n ).

"""
n = int(input("Digite um número: "))

i = 2
while i <= n:
    print(i)
    i += 2  # Incrementa de 2 em 2 para pegar apenas os pares