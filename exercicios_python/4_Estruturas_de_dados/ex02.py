"""
2. Dada uma lista de números inteiros, escreva um programa que calcula a soma de
todos os números na lista.
    Se preferir, pode utilizar a lista abaixo como exemplo:
    lista = [1, 10, 20, 35, 22, 12]
    # Resultado deve ser = 100
"""
lista = [1, 10, 20, 35, 22, 12]
soma = 0

# soma = sum(lista)

for num in lista:
    soma += num
    
print(soma)