"""
Dada uma lista de números inteiros, escreva um programa que encontre a soma dos números consecutivos maiores do que zero.
Por exemplo, para a lista [ -2, 3, 4, 0, 7, -1], o programa deve retornar a soma 7 (3 + 4).
"""

lista = [ -2, 3, 4, 0, 7, -1]
lista_positivos = []
soma = 0

for i in lista:
    if i >= 0:
        lista_positivos.append(i)

for j in lista_positivos:
    soma += j

print(lista)
print(f'A soma entre os numeros positivos da lista é de: {soma}')