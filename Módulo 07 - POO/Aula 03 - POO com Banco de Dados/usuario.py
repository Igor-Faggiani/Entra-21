"""Modelo de usuário"""

class Usuario:

    def __init__(self, nome: str, email: str, id: int = None):
        self.nome = nome
        self.email = email
        self.id = id
        
    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome} | Email: {self.email}"
    
    def __repr__(self):
        return f"ID: {self.id} | Nome: {self.nome} | Email: {self.email}"