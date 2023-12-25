from personagem import Personagem
from habilidade_especial import IHabilidadeEspecial

class Mago(Personagem, IHabilidadeEspecial):
    """Mago representa um personangem da classe Mago no jogo.
    
    Attributes:
        nome (str): Nome do mago.
        nível (str): Nível do mago.
        vida (str): Vida do mago.
    """
    
    def __init__(self, nome: str, nivel: int, vida: int, magia: int):
        super().__init__(nome, nivel, vida, magia)
        self.magia = magia # Atriuto específico do mago.
        
    def atacar(self):
        """Realiza a ação de atacar do mago."""
        super().atacar()
        print(f"{self.nome} Lança um feitiço poderoso com {self.magia} de magia.")
        
    def equipar_cajado(self):
        """Realiza a ação de quipar o cajado do mago."""
        print(f"{self.nome} equipe o seu cajado! O próximo ataque causará dano em área.")
        
    def usar_super_habilidade(self):
        """Utiliza super habilidade do mago."""
        print(f"{self.nome} Utiliza a habilidade especial Meteoro! Todos os inimigos perdem 99% da vida.")
    
if __name__ == "__main__":
    mago = Mago("Igor the Mage", 1, 10, 11)
    
    print(mago.nome)
    print(mago.magia)
    
    mago.atacar()
    mago.equipar_cajado()
    mago.usar_super_habilidade()