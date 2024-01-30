import sqlite3
from pokemon import Pokemon
from attack_repository import AttackRepository

class PokemonRepository():
    
    def __init__(self, db_name):
        self.db_name = db_name
        self.__repository_attack = AttackRepository(db_name)

    def __execute_query(self, query: str, *params: any):
        """Executa uma query no banco de dados.
        
        Args:
            query (str): Query que será executada.
            params (Any): Parâmetros da query.
        """
        connection = sqlite3.connect(self.db_name) # Abriu uma conexão com sqlite
        cursor = connection.cursor()
        cursor.execute(query, params) # Executar a query
        connection.commit() # Commitar as alterações feitas pela consulta
        connection.close() # Fecha a conexão com o banco de dados        


    def get_pokemon(self):
        """Obtem todos os pokemons cadastrados no banco de dados."""
        query = "SELECT id, name, health, type FROM pokemon;"
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        connection.close()
        
        pokemons = []
        for row in rows:
            pokemon = Pokemon(row[1], row[3], row[2], row[0])  # Ajuste da ordem dos parâmetros
            pokemons.append(pokemon)
        
        for i in range(len(pokemons)):
            print(pokemons[i])
    
    
    def choice_pokemon(self, pokemon: str):
        """Obtem todos os pokemons cadastrados no banco de dados."""
        query = "SELECT name, health, type FROM pokemon WHERE LOWER(name) = LOWER(?);"
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(query, (pokemon,))
        rows = cursor.fetchall()
        connection.close()
        

        if not rows:
                # Se a consulta não retornar resultados, você pode lançar uma exceção ou retornar None, dependendo do que deseja
                raise ValueError(f"Nenhum Pokémon encontrado com o nome: {pokemon}")

            # Certifique-se de que há pelo menos uma linha antes de acessar os elementos de 'rows'
        pokemon_data = rows[0]
        pokemon_name, pokemon_type, pokemon_health = pokemon_data

            # Agora você pode criar o objeto Pokemon
        pokemon = Pokemon(pokemon_name, pokemon_health, pokemon_type, self.__repository_attack.get_attack_pokemon(pokemon))

        return pokemon