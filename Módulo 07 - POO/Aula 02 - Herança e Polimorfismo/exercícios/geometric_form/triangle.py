from geometric_form import GeometricForm

class Triangle(GeometricForm):
    """Triangle representa um objeto em formato triangular.
    
    Attributes:
        base (float): base do triangulo.
        height (float): altura do triangulo.
        side1 (float): lado 1 do triangulo.
        side2 (float): lado 2 do triangulo.
        side3 (float): lado 3 do triangulo.
    """
    
    def __init__(self, base: float, height: float, side1 = float, side2 = float, side3 = float):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        
    def calculate_area(self):
        """Calcula a área do triangulo"""
        super().calculate_area()
        return self.base * self.height / 2
    
    def calculate_perimeter(self):
        """Calcula o perimetro do triangulo"""
        super().calculate_perimeter()
        return self.side1 + self.side2 + self.side3
    
if __name__ == '__main__':
    triangle = Triangle(3, 4, 3, 4, 5)
    
    print(f"A área do triangulo é: {triangle.calculate_area():.2f}")
    print(f"O perimetro do triangulo é: {triangle.calculate_perimeter():.2f}")
    
    