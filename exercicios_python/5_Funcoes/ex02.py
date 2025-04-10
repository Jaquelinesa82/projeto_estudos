"""
2. Implemente uma função que recebe uma lista de números inteiros e retorna uma
tupla (pos, num) , onde pos é a posição (ou índice) do maior número na lista e num
é o valor desse número.


pos = indice
num = valor
"""

def num_interios(lista):
    maior_num = lista[0]
    pos = 0
    for i in range(1, len(lista)):
        if lista[i] > maior_num:
            maior_num = lista[i]
            pos = i

    return (pos, maior_num)
    
numeros = (1, 10, 15, 40)
res = num_interios(numeros)
print(res)