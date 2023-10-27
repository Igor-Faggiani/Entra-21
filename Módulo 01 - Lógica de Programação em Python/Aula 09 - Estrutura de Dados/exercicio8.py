# Crie um dicionário de palavras em inglês e suas traduções
dicionario = {
    "hello": "olá",
    "world": "mundo",
    "good": "bom",
    "morning": "manhã"
}

texto_ingles = input("Digite um texto em inglês: ")

#Dividir o texto em palavras
palavras = texto_ingles.split()

#lista para armazenar as traduções
traducoes = []

# Traduza cada palavra do texto, se estiver no dicionário
for palavra in palavras:
    traducao = dicionario.get(palavra, palavra)
    traducoes.append(traducao)

texto_traduzido = " ".join(traducoes)

print("Texto traduzido:", texto_traduzido)
