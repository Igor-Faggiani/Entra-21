from pokemon import Pokemon
from attack import Attack

class PokemonRepository(Pokemon):

    def recive_damage(self, damage: float):
        """Função para o pokemon receber dano
        
        Args:
            damage (float): dano do pokemon
        """
        self.life -= damage
        
        input(f"{self.name} recebeu {self.damage} de dano!")
          
  
    def verify_hp(self):
        """Função para verificar se o pokemon está vivo"""
        if self.life > 0:
            return True
        else:
            return False