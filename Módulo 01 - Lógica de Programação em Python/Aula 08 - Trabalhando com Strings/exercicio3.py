"""
Faça um programa para anonimizar o nome completo
de uma pessoa ao substituir o último sobrenome com o caractere “#”.
"""

while True:
    nomes = input("Digite seu nome: ")

    #Transformar a String em vetor:
    palavras = nomes.split()

    #Verificar se á mais de 2 sobrenomes:
    if len(nomes) >= 2:

    #Anonimizar o ultimo sobrenome:
        sobrenome_anon = "*" * len(palavras[-1])

    #Reconstruir o nome completo com o ultimo sobrenome anonimizado:
    nome_anon = " ".join(palavras[:-1] + [sobrenome_anon])

    print(nome_anon)

else:
    print("O nome nõ contem sobrenome!!")