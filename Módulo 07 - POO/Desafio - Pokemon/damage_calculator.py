from abc import ABC
from pokemon import Pokemon
from attack import Attack

class DamageCalculator(ABC):
    """Calcula o dano recebido do pokemon"""
    
        
    def calculate_damage(self, chosen_attack: int, target):
        