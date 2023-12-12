from animal import Animals

class Bird(Animals):
    """Bird representa o animal Pássaro."""
    
    def make_sound(self):
        super().make_sound()
        print(f"{self.name} Sabia que o Sabiá sabia Subiá?")
        
    def move(self):
        super().move()
        print(f"{self.name} Deslocou-se até a Proway!")
        
if __name__ == '__main__':
    passarinho = Bird("João")
    
    passarinho.make_sound()
    passarinho.move()