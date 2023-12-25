from typing import Any, List
import sqlite3
from db_initialize import DatabaseInitialize
from pokemon import Pokemon

class DatabaseRepository:
    """Reresenta o repositório do banco de dados.
    
    Attributes:
        db_name (str): Nome do banco de dados.
    """
    
    def __init__(self, db_name):
        self.db_name = db_name
        
    def execute_query(self, query: str, *params: Any):
        """Executa uma query no banco de dados.
        
            Args:
                query (str): Query que será executada.
                params (Any): Parâmetros da Query.
        """
        
        connection = sqlite3.connect(self.db_name) # Abriu uma conexão com o sqlite
        cursor = connection.cursor()
        cursor.execute(query, params) # Executar a query
        connection.commit() # Commitar as alerações feitas pela consulta.
        connection.close() # Fecha a conexão com o banco de dados. 