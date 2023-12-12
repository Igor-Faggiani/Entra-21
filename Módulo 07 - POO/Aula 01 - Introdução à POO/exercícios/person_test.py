import pytest

from exercício01 import Person

def test_person_creation():
    person = Person("Igor Faggiani", "5547988692533")
    
    assert person.name == "Igor Faggiani"
    assert person.phone_number == "5547988692533"
    
def test_person_info(capfd):
    person = Person("Igor Faggiani", "5547988692533")
    person.person_info()
    
    #fornece as funções para acessar o terminal
    out,_= capfd.readouterr()
    
    assert out == "Nome: Igor Faggiani\nTelefone: 5547988692533\n"