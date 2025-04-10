"""
1. Escreva um programa que receba um número inteiro do usuário e imprima True
caso o número seja par e False, caso o número seja ímpar.
"""

num = int(input('Digite um inteiro: '))
resultado = num % 2 == 0

if num == True:
    print(f'Esse número {num} é par: {resultado}')
else:
    print(f'Esse número {num} é ímpar: {resultado}')