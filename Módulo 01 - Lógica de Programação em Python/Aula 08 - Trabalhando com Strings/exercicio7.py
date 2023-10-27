"""
 Escreva um algoritmo que encontre todas as ocorrências de números em uma string e os retorne em uma lista.
"""
import re

texto = input('Digite um texto: ')

padrao = r'\d+'
verificador = re.findall(padrao, texto)

print(verificador)