from abc import ABC, abstractmethod

class Animals(ABC):
    """Animals representa animais.
    
    Attributes:
        name (str): Nome do animal.
    """
    
    def __init__(self, name: str):
        self.name = name
     
    @abstractmethod   
    def make_sound(self):
        """Realiza a ação de emitir som."""
        pass
    
    @abstractmethod    
    def move(self):
        """Realiza a ação de mover."""
        pass