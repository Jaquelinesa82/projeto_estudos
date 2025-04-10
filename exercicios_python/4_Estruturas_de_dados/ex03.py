"""
3. Data uma lista de números inteiros, escreva um programa que calcula a média dos
números na lista. O resultado não deve incluir números decimais. Exemplo: 12.3
deve imprimir apenas 12 .
    Se preferir, pode utilizar a lista abaixo como exemplo:
    lista = [1, 10, 20, 35, 22, 12]
    # Resultado deve ser 16
    P.S.: Pode utilizar o operador // (divisão inteira)
"""
lista = [1, 10, 20, 35, 22, 12.3]
soma = 0

# soma = sum(lista)
for num in lista:
    soma += int(num)
    
media = soma // len(lista)
print(media)