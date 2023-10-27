"""
16. Escreva um algoritmo que peça o salário bruto de uma pessoa e imprima o salário líquido, segunda a tabela a seguir:

Salário bruto menor ou igual a R$ 600.00 - Isento
Salário bruto maior que R$ 600.00 e menor ou igual a R$ 1200.00 - 20%
Salário bruto maior que R$ 1200.00 e menor ou igual a R$ 2000.00 - 25%
Salário bruto maior que R$ 2000.00 - 30%
"""

salario_bruto = int(input("Digite o seu salário bruto: "))
if salario_bruto <= 0:
    print("Salário Invalido.")
elif salario_bruto <= 600:
    print(f"Isento. Salário líquido igual a R${salario_bruto:.2f} ")
elif 600 < salario_bruto <= 1200:
    print(f"Salário líquido igual a R${salario_bruto*0.8:.2f} ")
elif 1200 < salario_bruto <= 2000:
    print(f"Salário líquido igual a R${salario_bruto*0.75:.2f}")
else:
    print(f"Salário líquido igual a R${salario_bruto*0.7:.2f}")
