class Sistema_bancario:
    LIMITE_SAQUES = 3
    LIMITE_VALOR_SAQUE = 500.0

    def __init__(self, nome):
        self.nome = nome,
        self.saldo = 0.0
        self.extrato = ""
        self.numero_saques = 0
        self.total_saques = 0
    
    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato += f'Deposito: R$ {valor:.2f}\n'
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
        else:
            print('Operação falhou, o valor do depósito é inválido.')

    def saque(self, valor):
        if valor <= 0:
            print("Operação falhou! O valor do saque é inválido.")
        elif valor > self.saldo:
            print("Operação falhou! Saldo insuficiente.")
        elif valor + self.total_saques > self.LIMITE_VALOR_SAQUE:
            print("Operação falhou! O total dos saques excede o limite de R$ 500,00.")
        elif self.numero_saques >= self.LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")
        else:
            self.saldo -= valor
            self.total_saques += valor
            self.numero_saques += 1
            self.extrato += f"Saque: R$ {valor:.2f}\n"
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
                
    def mostrar_extrato(self):
        print('\n ================Extrato==============')
        print('Não fora realizadas movimentações.' if not self.extrato else self.extrato)
        print(f'\nSaldo atual: R$ {self.saldo:.2f}')
        print('========================================')

if __name__ == "__main__":
    cliente = Sistema_bancario("teste")

    cliente.deposito(2000)
    cliente.saque(200)
    cliente.saque(500)
    cliente.saque(100)
    cliente.mostrar_extrato()