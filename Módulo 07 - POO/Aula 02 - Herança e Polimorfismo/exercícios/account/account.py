from __future__ import annotations
from abc import ABC, abstractmethod
from random import randint

class Account(ABC):
    """Account representa uma conta bancária.
    
    Attributes:
        holder (str): Titular da conta.
    """
    
    def __init__(self,holder: str):
        self.__account_number = randint(1, 100_000)
        self.__balance = 0    
        self.holder = holder
       
    @property
    def account_number(self):
        """(int): Número da conta."""
        return self.__account_number
    
    @property
    def balance(self):
        """(float): Saldo da conta."""
        return self.__balance
    
    @balance.setter
    def balance(self, value: float):
        if value < 0:
            raise ValueError("O saldo não pode ser nengativo")
        self.__balance = value

    def withdraw(self, amount: float) -> bool:
        """Saca um valor da conta.
        
        Args:
            amount (float): Valor que será sacado.
            
        Returns:
            True caso o saque tenha sido realizado com sucesso, False caso contrário.
        """
        if self.__balance >= amount:
            self.__balance -= amount
            return True
        
        return False
    
    def deposit(self, amount: float):
        """Deposita um valort da conta
        
        Args:
            amount (float): valor que será depositado na conta.
        """
        tax = self.get_deposit_tax()
        
        self.__balance += amount * (1 - tax)
        
    def transfer(self, target_account: Account):
        """Transfere um valor para outra conta
        
        Args:
            amount (float): Valor que será transferido
            target_account (Account): Conta de destino da transferência.
        """
        if (self.withdraw(amount)):
            target_account.deposit(amount)
        else:
            print("Não foi possível realizar a transferência: Saldo indisponível!")
        
    @abstractmethod
    def get_deposit_tax(self) -> float:
        """Retorna a taxa de depósito."""