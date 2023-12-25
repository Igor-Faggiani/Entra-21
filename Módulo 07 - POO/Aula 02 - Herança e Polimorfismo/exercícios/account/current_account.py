from account import Account


class CurrentAccount(Account):
    """CurrentAccount representa a conta corrente."""

    def __init__(self, limit: int):
        super().__init__(limit)
        self.limit = limit      

    def deposit(self, value: float) -> None:
        super().deposit()	
        self.balance += value

    def withdraw(self, value: float) -> bool:
        super().withdraw()
        if (self.balance + self.limit) < value:
            print("Saldo insuficiente para realizar a operação.")
        return False

        if self.balance < value:
            self.limit -= value - self.balance
            self.balance = 0
        else:
            self.balance -= value
            
    def transfer(self, value: float, target_account: Account) -> None:
        super().transfer(value, target_account)
        
        if self.balance < value:
            print("Saldo insuficiente para realizar a operação")
        else:
            target_account.deposit(value)
            print("Transferência realizada com sucesso!")