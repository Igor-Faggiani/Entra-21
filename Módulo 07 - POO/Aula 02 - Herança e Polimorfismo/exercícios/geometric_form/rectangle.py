from geometric_form import GeometricForm

class Rectangle(GeometricForm):
    """Rectangle representa o objeto em formato retangular.
    
    Attributes:
        base (float): base do retangulo.
        height (float): altura do retangulo.
    """
    
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height
        
    def calculate_area(self):
        """Calcula a área do retangulo."""
        super().calculate_area()
        return self.base * self.height
    
    def calculate_perimeter(self):
        """Calcula o perimetro do retangulo."""
        super().calculate_perimeter()
        return 2 * (self.base + self.height)
    
if __name__ == '__main__':
    rectangle = Rectangle(4, 6)
    
    print(f"A área do retângulo é: {rectangle.calculate_area():.2f}")
    print(f"O perimetro do retângulo é: {rectangle.calculate_perimeter():.2f}")