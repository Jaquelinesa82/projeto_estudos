"""
1. Escreva uma função que recebe um número inteiro positivo e retorna True caso ele
seja primo e False , caso contrário.
Sugestão:
    def e_primo(n):
    # Sua implementação aqui
    print(e_primo(1))
    # False
    print(e_primo(2))
    # True
"""
def e_primo(n):
    if n < 2:
        return False
    else:
        for i in range(2, n): # 5 
            if n % i == 0:
                return False
                break
        else:
            return True

res = e_primo(n = 5)
print(res)