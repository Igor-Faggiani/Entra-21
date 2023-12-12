from animal import Animals

class Cat(Animals):
    """Cat representa o animal gato."""
    
    def make_sound(self):
        super().make_sound()
        print(f"{self.name} miou!")
        
    def move(self):
        super().move()
        print(f"{self.name} Moveu 100 Metros para frente!")
        
if __name__ == '__main__':
    gato = Cat("Dudinha")
    
    gato.make_sound()
    gato.move()