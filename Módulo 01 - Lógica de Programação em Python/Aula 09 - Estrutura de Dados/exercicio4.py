texto = input("Digite um texto: ")
palavras = texto.split()

dicionario = {}

for palavra in palavras:
    palavra = palavra.strip(".,!?").lower()

    if palavra in dicionario:
        dicionario[palavra] += 1
    else:
        dicionario[palavra] = 1

for palavra, contagem in dicionario.items():
    print(f"{palavra}: {contagem}")