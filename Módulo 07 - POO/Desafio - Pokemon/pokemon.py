from abc import ABC
from typing import List, Any
from attack import Attack
import time

class Pokemon(ABC):
    """Pokemon representa os pokemons.
    
    Attributes:
        name (str): Nome do pokemon
        type (str): Tipo do pokemon
        life (float): Vida do pokemon
        attack (Attack): Ataques do pokemon
    """
    
    def __init__(self, name: str, type: str, life: int, attacks: List[Attack]):
        self.__name = name
        self.__life = life
        self.__type = type
        self.__attacks = attacks
        
    @property
    def attacks(self):
        return self.__attacks
    
    @property
    def name(self):
        return self.__name
    
    @property
    def life(self):
        return self.__life
    
    @property
    def type(self):
        return self.__type
        
    def __str__(self):
        return f"Nome: {self.name} | Vida: {self.life} | Tipo {self.type}"
    
    
    def poke_attack(self, chosen_attack: int, target):
        """O pokemon ataca o alvo com um ataque específico.

        Args:
            chosen_attack (int): índice do ataque
            target (Pokemon): Pokemon alvo

        Returns:
            float: Dano causado pelo ataque
        """
        if not self.attacks:
            print(f"{self.name} não possui ataques para atacar.")
            return 0.0  # Retorna 0.0 se não houver ataques

        # Verifica se chosen_attack está dentro dos limites válidos
        if 0 <= chosen_attack < len(self.attacks):
            selected_attack = self.attacks[chosen_attack]
            print(f"{self.name} atacou {target.name} com {selected_attack.name} e recebeu {selected_attack.damage} de dano!")
            damage = selected_attack.calculate_damage()
            return damage
        else:
            print(f"{self.name} não possui um ataque com o ID {chosen_attack}.")
            return 0.0  # Retorna 0.0 se chosen_attack for inválido
        
       
    def verify_hp(self):
        """Função para verificar se o pokemon está vivo"""
        if self.life <= 0:
            self.life = 0
            print(f"O pokemon {self.name} está inconciente")
            return True
        else:
            print(f"O pokemon {self.name} está com {self.life} de HP")
            return False
        
        
    def show_attacks(self):
        """Função para mostrar os ataques do pokemon"""
        print(f"Ataques de {self.name}:")
        for attack in (self.attacks):
            print(f"{attack.name} | Dano: {attack.damage} | Tipo: {attack.type}")
            
    
