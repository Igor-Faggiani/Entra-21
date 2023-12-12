from abc import ABC

class Account(ABC):
    """Account representa uma conta bancária.
    
    Attributes:
        account_number (int): Número da conta.
        holder_name (str): Titular da conta.
        balance (float): Saldo da conta.
    """
    
    def __init__(self, account_number: int, holder: str, balance: float):
        self.account_number = account_number
        self.holder_name = holder
        self.balance = balance