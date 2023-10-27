"""
entrada de dados - etapa onde obtemos os dados
necessários para processar os passos do algoritimo.
"""
import sys
nome = input('Digite seu nome: ')
ano_nascimento = int(input('Digite o ano do seu nascimento: '))
ANO_ATUAL = 2023

# Para saber o tipo da variável
print(type(ANO_ATUAL))
print(type(ano_nascimento))
idade = ANO_ATUAL - ano_nascimento

# Para saber o tamanho da variável (espaço)
print(f'O tamanho da variável nome é: {sys.getsizeof(nome)} Bytes')
# Saída de dados (output)

print(f'O nome digitado foi {nome}')
print(f' Sua idade é de: {idade}')