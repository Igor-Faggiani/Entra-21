from exercício01 import Person

class PhoneBook:
    """PhoneBook representa uma agenda de contatos.
    
    Attributes:
        name (str): Nome da agenda.
    """
    
    def __init__(self, name: str):
        self.name = name
        self.__people = []
        
    
    def __str__(self) -> str:
        return f"Nome: {self.__name} | Telefone: {self.__phone_number}"
    
    @property
    def people(self):
        """(List][Person]): Liista de pessoas na agenda."""
        return self.__people
        
    def add_person(self, name: str, phone: str):
        """Adiciona uma pessoa na agenda
        
        Args:
            Person (Person): Pessoa que será adicionada na agenda.
        """
        person = Person(name, phone)
        if len(self.__people) < 10:
            self.__people.append(person)
        else:
            print("Agenda Lotada.")
            
    def remove_person(self, name: str):
        """Remove uma pessoa da agenda pelo nome
        
        Args:
            name (str): Nome da pessoa que será removida.
        """
        for person in self.__people:
            if person.name == name:
                self.__people.remove(person)
                return
                
        print("Pessoa não encontrada na agenda.")
        
    def search_person(self, name: str):
        for person in self.__people:
            if person.name == name:
                print(person)
                return
            
        print("Pessoa não encontrada na agenda.")
        
