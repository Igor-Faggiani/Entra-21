"""
 Escreva uma list comprehension que retorne uma lista dos quadrados dos números de 1 a 10.
"""

#Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#List comprehension
quadrados = [numero * 2 for numero in numeros]

print(quadrados)