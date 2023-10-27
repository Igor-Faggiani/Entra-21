"""
Escreva um programa que receba uma dlista como entrada e remova todas as duplicatas,
retornando uma nova lista com os elementos únicos em sua ordem original
"""

lista = [3, 3, 5, 6, 7, 8, 9, 9, 10]

lista_unica = list(set(lista))
print(lista_unica)
