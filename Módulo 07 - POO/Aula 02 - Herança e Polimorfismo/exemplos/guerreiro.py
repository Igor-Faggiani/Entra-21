from personagem import Personagem

class Guerreiro(Personagem):
    """Gerreiro representa um personangem da classe guerreiro no jogo.
    
    Attributes:
        nome (str): Nome do mago.
        nível (str): Nível do mago.
        vida (str): Vida do mago.
        forca (str): A quantidade de força do guerreiro.
    """
    
    def __init__(self, nome: str, nivel: int, vida: int, forca: int):
        super().__init__(nome, vida, forca)
        self.forca = forca # Atriuto específico do guerreiro.
        
    def atacar(self):
        """Realiza a ação de atacar do guerreiro."""
        super().atacar()
        print(f"{self.nome} Desfere um golpe poderoso com {self.forca} de força!")
        
    def equipar_escudo(self):
        """Realiza a ação de quipar o escudo do guerreiro."""
        print(f"{self.nome} equipe o seu escudo! A vida de {self.nome} aumentou.")
    
if __name__ == "__main__":
    guerreiro = Guerreiro("Igor the Warrior", 1, 50, 10)
    
    guerreiro.atacar()
    guerreiro.equipar_escudo()