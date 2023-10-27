"""
22. Faça um programa que leia a altura e o sexo (M ou F) de uma pessoa e calcule o peso ideal.
Para homens, o peso ideal é calculado pela fórmula: (72.7 * altura) - 58.
Para mulheres, o peso ideal é calculado pela fórmula: (62.1 * altura) - 44.7.
"""

altura = float(input("Digite a sua altura: "))
sexo = input("Qual o seu sexo? (M ou F): ")

if sexo == "M" or "m":
    print(f"O seu peso ideal é {(72.7 * altura) - 58:.2f}")
elif sexo == "F" or "f":
    print(f"O seu peso ideal é {(62.1 * altura) - 44.7:.2f}")
else:
    print("Você digitou um valor incorreto")
