from account import Account

class CheckingAccount(Account):
    """CheckingAccount representa uma conta corrente."""
    
    def __init__(self, holder: str, limit: float):
        super().__init__(holder)
        self.__limit = limit
    
    @property
    def limit(self):
        return self.__limit

    def withdraw(self, amount: float) -> bool:
        """Saca um valor da conta.
        
        Args:
            amount (float): Valor que será sacado.
            
        Returns:
            True caso o saque tenha sido realizado com sucesso, False caso contrário.
        """
        if (self.balance) < amount:
            print("Saldo insuficiente para realizar a operação.")
            return False

        if self.balance < amount:
            self.__limit -= valor - self.balance
            self.balance = 0
        else:
            self.balance -= amount

        return True
    
    def get_deposit_tax(self) -> float:
        return 0.002
    
if __name__ == "__main__":
    checking_account = CheckingAccount("Igor", 100)
    checking_account.deposit(1000)
    checking_account.withdraw(10)
    
    checking_account2 = CheckingAccount("Roedel", 50)
    checking_account.transfer(50, checking_account2)
    
    print(checking_account.limit)
    print(checking_account2.balance)