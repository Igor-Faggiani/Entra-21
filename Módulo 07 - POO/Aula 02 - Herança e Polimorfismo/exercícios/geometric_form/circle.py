from geometric_form import GeometricForm

class Circle(GeometricForm):
    """Circle representa um objeto em formato circular.
    
    Attributes:
        raio (float): Raio do círculo.
    """
    
    def __init__(self, raio: float):
        self.raio = raio
        
    def calculate_area(self):
        """Calcula a área do círculo"""
        super().calculate_area()
        return 3.14 * self.raio ** 2
    
    def calculate_perimeter(self):
        """Calcula o perímetro do círculo"""
        super().calculate_perimeter()
        return 2 * 3.14 * self.raio
    
if __name__ == '__main__':
    pizza = Circle(5)
    
    print(f"Área do círculo: {pizza.calculate_area():.2f} Metros")
    print(f"Parâmetro do círculo: {pizza.calculate_perimeter():.2f} Metros")