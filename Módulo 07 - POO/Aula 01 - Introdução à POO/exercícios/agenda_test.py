import pytest

from exercício01 import Person
from exercício03 import PhoneBook


def test_add_person():
    phone_book = PhoneBook("Agenda de contatos.")
    
    phone_book.add_person("Igor Faggiani", "5547988692533")
    
    assert len(phone_book.people) == 1
    assert phone_book.people[0].name == "Igor Faggiani"
    
def test_remove_person():
    phone_book = PhoneBook("Agenda de contatos.")
    
    phone_book.add_person("Igor Faggiani", "5547988692533")
    assert len(phone_book.people) == 1
    
    phone_book.remove_person("Igor Faggiani")
    assert len(phone_book.people) == 0
    
def test_add_person_failed(capfd):
    phone_book = PhoneBook("Agenda de contatos.")
    
    for i in range(10):
        phone_book.add_person(f"Pessoa {i}", f"5547988692533{i}")
        
    phone_book.add_person("Extra", "+5 (47) 99999-9999")
    out, _ = capfd.readouterr()
    
    assert "Agenda Lotada.\n" in out