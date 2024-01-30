from typing import Any, List
import sqlite3
from attack import Attack
from db_initialize import DatabaseInitialize

class AttackRepository:
    
    def __init__(self, db_name):
        self.db_name = db_name

    def __execute_query(self, query: str, *params: Any):
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


    def get_attack(self):
        """Obtem todos os ataques cadastrados no banco de dados."""
        
        query = "SELECT id, name, type, damage FROM attack;"
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        connection.close()
        
        attacks = []
        for row in rows:
            attack = Attack(row[0], row[1], row[3], row[2])  # Ajuste da ordem dos parâmetros
            attacks.append(attack)
        
        return attacks
    
  
    def get_attack_pokemon(self, pokemon: str):
        """Obtem todos os ataques de um pokemon cadastrado no banco de dados.""" #verificar qual o id do pokemon
        query = """SELECT attack.id, attack.name, attack.damage, attack.type
                FROM attack
                JOIN pokemon ON pokemon_attack.pokemon_id = pokemon.id
                JOIN pokemon_attack ON attack.id = pokemon_attack.attack_id
                WHERE LOWER(pokemon.name) = LOWER(?)"""
        
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute(query, (pokemon,))
        rows = cursor.fetchall()
        connection.close()
        
        attacks = []
        for row in rows:
            attack = Attack(row[0], row[1], row[2], row[3]) # Ajuste da ordem dos parâmetros
            attacks.append(attack)
            

        return attacks
    
