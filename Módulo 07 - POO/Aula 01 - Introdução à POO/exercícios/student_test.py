import pytest
from exercício02 import Student  # Supondo que a classe Student está definida em um arquivo student.py

def test_student_creation():
    student = Student("12345", "Lucas", [6.7, 9.8, 5.4, 10, 8.3])
    assert student.registration_number == "12345"
    assert student.name == "Lucas"
    assert student.grade == [6.7, 9.8, 5.4, 10, 8.3]

def test_get_media():
    student = Student("12345", "Lucas", [6.7, 9.8, 5.4, 10, 8.3])
    assert student.get_media() == pytest.approx(8.04)

def test_get_situacao_aprovado():
    student = Student("12345", "Lucas", [6.7, 9.8, 5.4, 10, 8.3])
    assert student.get_situacao() == "Aprovado!"

def test_get_situacao_recuperacao():
    student = Student("12345", "Lucas", [6.7, 5.5, 5.0])
    assert student.get_situacao() == "Recuperação!"

def test_get_situacao_reprovado():
    student = Student("12345", "Lucas", [4.5, 3.0, 2.5])
    assert student.get_situacao() == "Reprovado!"

def test_get_media_with_empty_grades():
    student = Student("12345", "Lucas", [])
    assert student.get_media() == 0
