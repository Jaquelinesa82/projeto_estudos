"""
Exercício: Somar os números de 1 até 10 (inclusive)
"""
soma = 0
for i in range(1, 11):# vai de 1 até 10
    soma += 1

print(f'A soma dos números é: {soma}')

"""
Mais um exercício com passo de 2:
Agora, vamos usar o passo de 2 para somar apenas os números ímpares entre 1 e 10.
"""
soma_impares = 0
for i in range(1, 11, 2):# Vai de 1 até 09, pulando de 2 em 2
    soma_impares += i
print(f'A soma dos números ímpares é: {soma_impares}')