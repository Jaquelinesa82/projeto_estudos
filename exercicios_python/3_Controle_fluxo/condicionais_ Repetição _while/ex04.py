"""
4. O jogo “Acerte o número” funciona da seguinte maneira:
    a. Existe um certo número inteiro declarado dentro do programa que o usuário
    desconhece. Por exemplo: numero = 8
    b. O usuário tem 3 tentativas para acertar o número.
    c. A cada tentativa, é informado ao usuário se o número que ele digitou é maior,
    menor, ou igual ao número correto.
    d. O jogo termina quando o usuário erra 3 vezes (perdeu) ou quando o usuário
    acerta o número (ganhou).
    Implemente o jogo “Acerte o número”.
"""
numero_certo = 10
tentativas = 3

while tentativas > 0:
    num = int(input('Digite um número:'))
    if num < numero_certo:
        print('Esse número e menor que o número correto.')
    elif num > numero_certo:
        print('Ese número e maior que o número correto.')
    else:
        print(f'VC ganhou!!!, o número digitado:{num} e igual ao {numero_certo}')
        break
    tentativas -= 1
    
    if tentativas == 0:
        print('Acabou as tentativas')
