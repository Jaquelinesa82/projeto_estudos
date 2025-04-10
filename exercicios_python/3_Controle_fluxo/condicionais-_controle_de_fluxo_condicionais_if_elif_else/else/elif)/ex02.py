"""
2. Implemente uma calculadora que recebe 3 valores do usuário:
    a. Operando a (pode ser um inteiro ou float).
    b. Operando b (pode ser um inteiro ou float).
    c. Operador op .
        i.
        pode ser uma string representando o operador, por exemplo, "+" ou "-
        ". Outra opção é utilizar números, por exemplo, 1 para soma , 2 para
        subtração , etc.
    
    O seu programa deve receber esses 3 valores e imprimir o resultado da operação.
    Caso o operador seja de divisão e o segundo operando seja o valor zero, o
    programa deve imprimir uma mensagem: “Não é possível realizar divisão por
    zero!”.

"""  
a = float(input('Digite um valor: '))
b = float(input('Digite outro valor: '))
op = input('Digite Calculadora \n 1 = + \n 2 = - \n 3 = * \n 4 = / : ').isdigit()

if op in ('+', 1):
    print(a + b)
elif op in ('-', 2):
    print(a - b)
elif op in ('*', 3):
    print(a * b)
elif op in ('/', 4):
    if op == 0:
        print('Não e possível realizar operação por zero.')
    else:
        print(a / b)
else:
    print(f'Operador inválido!')