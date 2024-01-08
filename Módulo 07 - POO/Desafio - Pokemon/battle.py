from pokemon import Pokemon
from random import choice

class Battle:
    def __init__(self, pokemon1: Pokemon, pokemon2: Pokemon):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.turno = 1
    