from abc import ABC

class Attack(ABC):
    """Attack representa um tipo de ataque
    
    Attributes:
        name (str): nome do ataque
        damage (float): dano do ataque
        type (str): tipo do ataque
    """
    def __init__(self, id: int, name: str, damage: int, type: str):
        self.__id = id
        self.__name = name
        self.__damage = damage
        self.__type = type
        
    def __str__(self) -> str:
        return f"{self.name} Dano: {self.damage} | type: {self.type}"
    
    def calculate_damage(self):
        return self.__damage
    
    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def damage(self):
        return self.__damage
    
    @property
    def type(self):
        return self.__type