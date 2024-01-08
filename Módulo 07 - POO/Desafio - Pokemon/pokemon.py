from attack import Attack

class Pokemon:
    """Pokemon representa os pokemons.
    
    Attributes:
        name (str): Nome do pokemon
        type (str): Tipo do pokemon
        life (float): Vida do pokemon
        attack (Attack): Ataque do pokemon
    """
    
    def __init__(self, name: str, type: str, life: float, *attacks: Attack):
        self.name = name
        self.life = life
        self.type = type
        self.attacks = attacks
        
    def __str__(self):
        return f"Nome: {self.name} | Vida: {self.life} | Tipo {self.type} | Ataque {self.attacks}"