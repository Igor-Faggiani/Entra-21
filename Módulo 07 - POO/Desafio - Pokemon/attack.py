from pokemon import Pokemon

class Attack:
    def __init__(self, id: int, name: str, damage: float, type: str):
        self.id = id
        self.name = name
        self.damage = damage
        self.type = type
        
    def __str__(self) -> str:
        return f"ID: {self.id} | Nome: {self.name} | Dano: {self.damage} | Tipo: {self.type}"
    
    def __repr__(self) -> str:
        return f"Nome: {self.name}"