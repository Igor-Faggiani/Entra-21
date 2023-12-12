class Person:
    """ Person representa uma pessoa"""
    
    def __init__(self, name: str, phone_number: str):
        self.name = name
        self.phone_number = phone_number
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    #acesso ao valor da propriedade privada
    @property
    def phone_number(self):
       return self.__phone_number
   
   #setter atualiza
    @phone_number.setter
    def phone_number(self, phone_number):
        self.__phone_number = phone_number
       
       
    def person_info(self):
        print(f"Nome: {self.__name}")
        print(f"Telefone: {self.__phone_number}")
        

if __name__ == "__main__":
    person = Person("Igor Faggiani", "47988692533")
    person.person_info()
    
    person.name = "William"
    person.phone_number = "999999999"
    print(person.name)
    print(person.phone_number)