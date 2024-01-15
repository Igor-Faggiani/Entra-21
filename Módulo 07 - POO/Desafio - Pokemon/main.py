from db_initialize import DatabaseInitialize
from pokemon_repository import PokemonRepository
from attack_repository import AttackRepository
from battle import Battle
from pokemon import Pokemon
from attack import Attack

db_name = "pokemon.sqlite"

pokemon_repository = PokemonRepository(db_name)
attack_repository = AttackRepository(db_name)

pokemon_repository.get_pokemon()
attacks = attack_repository.get_attack()

battle = Battle()
game_phase = 0
chosen_attack = 0
print("""----------------------------------------------------------------""")


# repository_attack = AttackRepository(db_name)

while True:
    match game_phase:
        case 0:
            
            pokemon1 = input("Escolha o seu pokemon favorito: ")
            pokemon2 = input("Escolha o pokemon adversário: ")
            
            try:
                pokemon1 = pokemon_repository.choice_pokemon(pokemon1)
                pokemon2 = pokemon_repository.choice_pokemon(pokemon2)
                game_phase += 1
            except:
                print("Não foi encontrado o pokemon selecionado")
                
        case 1:
            print("----------------------------------------------------------------")
            print(f"""A babtalha começou!
                    {pokemon1.name} VS {pokemon2.name}
                    """)
            if battle.battle_inverter():
                pokemon1.show_attacks()
                chosen_attack = int(input("Escolha o ataque: "))
                while chosen_attack > len(pokemon1.attacks) or chosen_attack < 1:
                    print("Por favor escolha um ataque existente.")
                    chosen_attack = int(input("Escolha o ataque: "))
                    
            damage = pokemon1.poke_attack(chosen_attack -1, pokemon2)
            if pokemon2.verify_hp():
                battle.skip_turn()
                print(f"Vitória do {pokemon1.name}")
                
        case 2:
            print("----------------------------------------------------------------")
            print(f"""A batalha continua!
                    {pokemon1.name} VS {pokemon2.name}
                    """)

            if battle.battle_inverter():
                pokemon2.show_attacks()
                chosen_attack = int(input("Escolha o ataque: "))
                while chosen_attack > len(pokemon2.attacks) or chosen_attack < 1:
                    print("Por favor escolha um ataque existente.")
                    chosen_attack = int(input("Escolha o ataque: "))

                pokemon2.poke_attack(chosen_attack, pokemon1)
                if pokemon1.take_damage():
                    pokemon1.verify_hp()

                game_phase += 1
                
        case _:
            break