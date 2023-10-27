"""
Escreva um programa que receba uma lista de palavras e retorne a palavra mais longa.
"""

palavras = ['caderno', 'penal', 'parede', 'garrafinha', 'teclado', 'pneumoultramicroscopicossilicovulcanoconiótico']
maior_palavra = " "

for m in palavras:
    if len(m) > len(maior_palavra):
        maior_palavra = m

print(f'A maior palavra é: {maior_palavra}')