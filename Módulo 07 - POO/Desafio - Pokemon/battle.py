from abc import ABC
from pokemon import Pokemon
from attack import Attack
import random

class Battle(ABC):
    """Battle representa a batalha entre 2 pokemons, um escolhido pelo jogador, e outro pela máquina
    
    Attributes:
        pokemon1: O pokemon escolhido pelo jogador
        pokemon2: O pokemon escolhido pela máquina
    """
    
    def __init__(self):
        self.__turn = True

        
    
    def end_game(self, pokemon1: Pokemon, pokemon2: Pokemon):
        """end_game representa o fim da batalha definindo o vencedor e o perdedor
        
        Args:
            pokemon1 (Pokemon): Pokemon vencedor
            pokemon2 (Pokemon): Pokemon perdedor
        """
        
        self.__pokemon1 = pokemon1
        self.__pokemon2 = pokemon2
        
    def battle_inverter(self):
        """Alterna entre o jogador1 e o jogador2"""
        if self.__turn: # False
            self.__player_turn = 1
            print(f"Jogador 1 está atacando:")
        else: # True
            self.__player_turn = 2
            print(f"Jogador 2 está atacando:")
        self.__turn = not self.__turn
        
        return self.__turn, self.__player_turn  # Agora retornamos também qual jogador está atacando

    # def battle_inverter(self):
    #     """Alterna entre o jogador e a máquina"""
    #     self.__turn = not self.__turn
    #     if self.__turn:
    #         print(f"Jogador 1 está atacando:")
    #     else:
    #         print(f"Jogador 2 está atacando:")
        
    #     return self.__turn
    
    def skip_turn(self):
        pass
    
    # Lógica para aplicar os danos