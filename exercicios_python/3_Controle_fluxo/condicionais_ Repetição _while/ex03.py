from sympy import isprime


"""
3. Um número primo é um número que é divisível apenas por 1 e por ele mesmo.
Escreva um programa que receba um número n e informe se esse número é primo
ou não.

"""
num = int(input('Digite um número: '))

# if num < 2:
#     print(f'{num} não e um número primo')
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print(f'{num} não é um número primo')
#             break
#         else:
#             print(f'{num} é um número primo')

#Usando a biblioteca sympy já verifica se o número e primo
if isprime(num):
    print(f'{num} é um número primo.')
else:
    print(f'{num} não é um número primo.')
