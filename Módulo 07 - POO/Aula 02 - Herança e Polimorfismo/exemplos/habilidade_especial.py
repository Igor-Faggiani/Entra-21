from abc import ABC, abstractmethod

class IHabilidadeEspecial(ABC):
    """IHabilidadeEspecial é uma interface que define as habilidades especiais que os personagens devem ter."""
    
    @abstractmethod
    def usar_super_habilidade(self):
        """Utiliza a super habilidade do personagem."""