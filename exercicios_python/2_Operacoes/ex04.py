""" 
Alice é responsável por escrever um programa que verifica se um cupom de
desconto pode ser utilizado. O programa recebe 3 valores e retorna True caso o
cupom possa ser utilizado, ou False , caso contrário.
Os três valores que o programa recebe são:
1. Valor de compra (float)
2. Valor do frete (float)
3. Cliente é cadastrado no programa de fidelidade (string “s” (sim) ou “n” (não))
O cupom tem a seguinte regra:
Caso o valor da compra somado ao frete seja superior a R$
100, ou o cliente seja cadastrado no programa de fidelidade, o
cupom de desconto pode ser utilizado. Caso contrário, o cupom
não pode ser utilizado.
Seu objetivo é implementar o programa que atenda a especificação acima.
"""
valor_compra = float(input('Digite o valor da compra: R$ '))
valor_frete = float(input('Digite o valor do frete: R$ '))
cadastrar_cliente = str(input('Cliente cadastrado(s/n): ')).strip().lower()
valor_total = valor_compra + valor_frete

if valor_total >= 100:
    cadastrar_cliente = True
    print(f'Cliente cadastrado no programa fidelidade com sucesso.')
else:
    print(f'Cliente não participa do programa fidelidade.')

