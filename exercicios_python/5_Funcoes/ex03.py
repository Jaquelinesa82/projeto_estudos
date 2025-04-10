"""
3. Implemente uma função maior_idade(pessoa) que receba uma tupla representando
uma pessoa com nome e idade e imprime na tela se a pessoa é maior de idade ou
não.
"""
def maior_idade(pessoa):
    nome, idade = pessoa

    if idade >= 18:
        print(f'{nome} com {idade} é maior de idade.')
    else:
        print(f'{nome} com {idade} e menor de idade.')
    
    return nome, idade


pessoa = ('jaque', 15)
res = maior_idade(pessoa)
