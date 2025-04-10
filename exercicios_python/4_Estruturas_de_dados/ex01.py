"""
1. Escreva um programa que lê números inteiros positivos do usuário, um após o
outro, e monta uma lista a partir desses números e depois imprime a lista montada.
O programa deve continuar solicitando por números até que o elemento digitado
seja um número negativo (que não deve ser inserido na lista).
"""

lista = []

while True:
    num = int(input('Digite números: '))
    
    if num < 0:
        print(f'Esse {num} é negativo')
        break
    
    lista.append(num)
    print(f'Lista: {lista}')

print(f'Lista de números: {lista}')

