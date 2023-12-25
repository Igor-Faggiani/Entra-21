from account import Account

class SavingsAccount(Account):
    """SavingsAccount representa uma conta bancária."""
    interest_percentage = 0.58
    
    def __init__(self, holder: str, initial_balance: float):
        super().__init__(holder)
        self.initial_balance = initial_balance
        self.deposit(initial_balance)
            
    def generate_interest(self):
        """Gera o juros mesal da conta."""
        self.balance += self.balace * (SavingsAccount.interest_percentage / 100)
        
    def get_deposit_tax(self) -> float:
        return 0.005
    
if __name__ == '__main__':
    savings_account = SavingsAccount("Igor", 1000)
    savings_account.deposit(500)
    print(savings_account.balance)