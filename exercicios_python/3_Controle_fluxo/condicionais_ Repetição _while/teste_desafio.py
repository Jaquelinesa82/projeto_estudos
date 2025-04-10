class PaymentProcessor:
    def __init__(self):
        self.accounts = {}  # Dicionário para armazenar contas e seus saldos

    def create_account(self, account_id, va=0, vr=0, cash=0):
        """Cria uma conta com saldos iniciais."""
        self.accounts[account_id] = {"va": va, "vr": vr, "cash": cash}

    def process_transaction(self, transaction):
        """Processa uma transação e retorna o resultado."""
        account_id = transaction["account"]
        amount = transaction["amount"]
        category = transaction["category"]

        if account_id not in self.accounts:
            return {"status": "rejeitada", "motivo": "conta inexistente"}

        # Determinar saldo a ser usado
        saldo_tipo = self.get_balance_type(category)
        if saldo_tipo not in self.accounts[account_id] or self.accounts[account_id][saldo_tipo] < amount:
            return {"status": "rejeitada", "motivo": "saldo insuficiente"}

        # Debitar saldo e aprovar transação
        self.accounts[account_id][saldo_tipo] -= amount
        return {"status": "aprovada", "motivo": "saldo debitado"}

    def get_balance_type(self, category):
        """Determina qual saldo deve ser usado com base no MCC (código da categoria)."""
        if category in [5411, 5412]:  # Supermercado
            return "va"
        elif category == 5811:  # Restaurante
            return "vr"
        return "cash"  # Qualquer outra categoria usa dinheiro

# Teste simples
processor = PaymentProcessor()
processor.create_account("user1", va=100, vr=50, cash=200)

transacoes = [
    {"account": "user1", "amount": 30, "category": 5411},  # Usa VA
    {"account": "user1", "amount": 60, "category": 5811},  # Usa VR (saldo insuficiente)
    {"account": "user1", "amount": 150, "category": 1234},  # Usa CASH
]