"""
Faça um programa que receba uma lista de números inteiros e retorne uma nova lista com os elementos em ordem crescente.
"""
lista_numeros = []

for i in range(5):
    numeros = int(input('Digite um número: '))
    lista_numeros.append(numeros)

lista_numeros.sort()
print(lista_numeros)