from animal import Animals

class Dog(Animals):
    """Dog representa o animal cachorro."""
    
    def make_sound(self):
        super().make_sound()
        print(f"{self.name} latiu!")
        
    def move(self):
        super().move()
        print(f"{self.name} Moveu 10 Metros à frente.")
    
if __name__ == "__main__":
    animal = Dog("Roedel")
    
    animal.make_sound()
    animal.move()