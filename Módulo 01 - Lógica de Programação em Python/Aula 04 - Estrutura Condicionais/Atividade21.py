"""
21. Faça um programa que leia a idade de uma pessoa e exiba se ela é criança (até 12 anos),
adolescente (13 a 17 anos), adulto (18 a 59 anos) ou idoso (maiores de 60 anos).
"""

idade = int(input("Digite a sua idade: "))
if idade < 0:
    print("Idade inválida")
elif idade <= 12:
    print("Criança.")
elif 13 <= idade <= 17:
    print("Adolescente.")
elif 18 <= idade <= 59:
    print("Adulto.")
else:
    print("Idoso.")
