"""
6. DESAFIO. Uma função fatorial calcula o valor da multiplicação de um certo número
inteiro não-negativo por todos os números positivos menores que ele. A exceção é
o fatorial de zero que é igual a 1. Por exemplo:
    fatorial(3) = 3 * 2 * 1 = 6
    fatorial(1) = 1
    fatorial(0) = 1
    Ou seja, podemos definir a função fatorial como:
"""
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

print(fatorial(3))  # 6
print(fatorial(1))  # 1
print(fatorial(0))  # 1
