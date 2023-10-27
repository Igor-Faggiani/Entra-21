nome = input('Digite seu nome: ')

quantidade_de_vogais = 0
quantidade_de_letras = len(nome)

for letra in nome:
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        quantidade_de_vogais += 1

quantidade_de_consoantes = quantidade_de_letras - quantidade_de_vogais
print(f"""
Quantidade de Vogais: {quantidade_de_vogais}
Quantidade de Consoantes: {quantidade_de_consoantes}
Quantidade de Letras: {quantidade_de_letras}
""")