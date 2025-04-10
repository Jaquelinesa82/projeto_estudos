"""
8. DESAFIO. Escreva um programa que declara uma lista com elementos de
diferentes tipos e imprime na tela essa lista invertida. Não é permitido utilizar
métodos como reverse ou sort .
    def inverte_lista(lista):
    ...
    lista = ["a", 5, {1}]
    lista_invertida = inverte_lista(lista)
    print(lista_invertida)
    # [{1}, 5, "a"]   
"""
def inverte_lista(lista):
    return lista[::-1]
    
lista = ["a", 5, {1}]
lista_invertida = inverte_lista(lista)
print(lista_invertida)