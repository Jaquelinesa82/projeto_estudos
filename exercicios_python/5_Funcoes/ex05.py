"""
5. Implemente uma função que recebe dois argumentos, uma lista e um elemento , e
retorna True caso elemento seja encontrado na lista , e False caso contrário. Não
é permitido utilizar o método in .
"""
def dois_argumento(lista, elemento):
    for item in lista:
        if item == elemento:
            return True
        
    return False
    
lista = [1, 2, 3]
elemento = 'jaque'
resposta = dois_argumento(lista, elemento)
print(resposta)   