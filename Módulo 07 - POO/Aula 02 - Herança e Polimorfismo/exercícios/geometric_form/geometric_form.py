from abc import ABC, abstractmethod

class GeometricForm(ABC):
    """GeometricForm representa a forma geométrica de um objeto."""
    
    @abstractmethod
    def calculate_area(self):
        """Calcula a area do objeto."""
        pass
    
    @abstractmethod
    def calculate_perimeter(self):
        """Calcula o perimetro do objeto."""
        pass
