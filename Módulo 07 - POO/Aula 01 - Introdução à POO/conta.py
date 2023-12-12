"""Implementação da Conta."""
from __future__ import annotations

class Conta:
    """Conta representa uma conta bancária.
    
    Attributes:
    numero (str): Número identificador da conta.
    titular (str): Nome do titular da conta.
    saldo (float): Saldo da conta.
    limite (float): Limite da conta.
    """

    quantidade_contas = 0 # Atributo estático --> pertence a classe e não ao objeto

    def __init__(self, numero: str, titular: str):
        # Verificando se a conta tem 9 digitos:
        if len(numero) != 9:
            raise AttributeError("número da conta deve conter 9 dígitos")
        
        # Encapsulamento
        self.__numero = numero
        self.titular = titular # Está usando o @titular.setter para definir o valor
        self.__limite = 100
        self.__saldo = 0

        Conta.quantidade_contas += 1

    def __str__(self):
        return f"titular: {self.__titular} | Saldo: {self.__saldo} | Limite: {self.__limite}"

    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self, novo_titular: str):
        self.__titular = novo_titular.title()

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite: float):
        self.__limite = novo_limite

    @property
    def saldo(self):
        return self.__saldo

    def depositar(self, valor: float) -> None:
        """deposita um valor no saldo da conta
        
        Args:
        valor (float): Valor do deposito
        """
        self.__saldo += valor

    def sacar(self, valor: float) -> bool:
        """Saca um valor da conta se o salto + limite for maior ou igual ao valor do saque.
        
        Args:
        valor (float): Valor do saque.

        Returns:
        True se for bem-sucedido, Flase caso contrário.
        """
        if (self.__saldo + self.__limite) < valor:
            print("Saldo insuficiente para realizar a operação.")
            return False

        if self.__saldo < valor:
            self.__limite -= valor - self.__saldo
            self.__saldo = 0
        else:
            self.__saldo -= valor

        return True
    
    def transferir(self, valor: float, conta_destino: Conta) -> None:
        """Transfere o valor de uma conta para outra se o (saldo + limite)
        for maior ou igual ao valor do saque.
        
        Args:
        valor (float): Valor da transferência.
        conta_destino (Conta): Conta de destino da transferência.
        """
        if (self.sacar(valor)):
            conta_destino.depositar(valor)
            print("Transferência relaizada com sucesso.")
        
    @staticmethod
    def verifica_numero_conta(numero: str) -> bool:
        """Verufucar se o número da conta é válido.
        
        Args:
            numero (str): Número da conta.
            
        Returns:
            True caso o número da conta seja válido, False caso contrário.
        """
        return numero != 9


if __name__ == "__main__":
    conta_igor = Conta("123456789", "igor")

    print(f"Nome do titlar quando a conta foi criada: {conta_igor.titular}")

    conta_igor.titular = "Igor Faggiani"

    print(f"Nome do titular depois de criada: {conta_igor.titular}")

    print(f"Vlor antes do depósito: {conta_igor.saldo}")
    conta_igor.depositar(100_000_000)
    print(f"Valor após o depósito: {conta_igor.saldo}")
    conta_igor.sacar(100_000_0011)
    conta_igor.sacar(100)
    print(f"Valor após o saque: {conta_igor.saldo} | Limite: {conta_igor.limite}")
    print(conta_igor)
    conta_igor.sacar(99999900)
    print(f"Valor após o saque: {conta_igor.saldo} | Limite: {conta_igor.limite}")

    conta_marcos = Conta("123467282", "marcos")
    print(conta_marcos)

    conta_igor.transferir(20, conta_marcos)
    print(conta_igor)
    print(conta_marcos)

    print(f"Quantidade de contas: {Conta.quantidade_contas}")

    if(Conta.verifica_numero_conta("12318371")):
        print("Número da conta é válido!")
    else:
        print("Número da conta é inválido!")