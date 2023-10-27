"""
Tupla é uma coleção ordenada e imutável de elementos.
"""

# Criando uma tupla
frutas = ("Maçã", "Banana", "Cereja")

# Imutabilidade
# frutas[0] = "Abacate" # Error

# Acesso aos elementos
print(frutas[0])

# Ordenando uma tupla
frutas_ordenadas = tuple(sorted(frutas))
print(frutas_ordenadas)

"""
Exemplo 1)

Faça um algoritmo que receba um número inteiro de 1 à 12 e mostre o mês
correspondente
"""
meses = (
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro"
)

mes = int(input("Digite um número inteiro de 1 à 12: "))

if 1 <= mes <= 12:
    print(meses[mes - 1])
else:
    print("Mês inválido!")
