from personagem import Personagem
from guerreiro import Guerreiro
from mago import Mago

class Combate:
    """Comabate representa uma partida do jogo.
    
    Attributes:
        personagem1 (Personagem): Personagem 1.
        personagem2 (Personagem): Personagem 2.
    """
    
    def __init__(self, personagem1: Personagem, personagem2: Personagem):
        self.persoagem1 = personagem1
        self.persoagem2 = personagem2
        
    def iniciar_combate(self):
        """Inicia o combate entre dois personagens."""
        print(f"Início do combate entre {self.persoagem1.nome} e {self.persoagem2.nome}")
        
        self.persoagem1.atacar()
        self.persoagem2.defender()
    
        self.persoagem2.atacar()
        self.persoagem1.defender()
    
        self.persoagem1.atacar()
        self.persoagem2.morrer()
        
        print("Fim do combate")
        
if __name__ == "__main__":
    igor_mage = Mago("Igor the Mage", 1, 10, 10)
    will_warrior = Guerreiro("William the Warrior", 1, 50, 10)
    
    combate = Combate(igor_mage, will_warrior)
    combate.iniciar_combate()
    
    #Herança