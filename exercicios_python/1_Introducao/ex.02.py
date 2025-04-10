"""
Escreva um programa com as seguintes especificações:
Uma variável “valor_compras” que receba um valor do tipo float, representando
o valor total das compras.
Uma variável “desconto” que receba um valor do tipo float, representando o
desconto a ser aplicado sobre o valor total das compras.
Uma variável “quantidade_itens”, que represente a quantidade de itens que
foram comprados.
Seu programa deve imprimir dois resultados:
1. O valor final das compras, considerando o desconto aplicado.
2. O custo médio de cada item (considerando o valor final das compras).
"""
valor_compras = float(input('Digite  o valor total da compra R$: '))
desconto = float(input('Digite o valor de desconto: '))
qtd_itens = 20
valor_final = valor_compras - desconto
custo_medio = valor_final / qtd_itens  if qtd_itens > 0 else 0

print(f'Valor final da compra: R${valor_final:.2f}')
print(f'Custo médio de cada item R${custo_medio:.2f}')
