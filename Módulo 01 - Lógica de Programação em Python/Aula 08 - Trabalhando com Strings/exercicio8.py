texto = input('Digite um texto: ')
palavra = list(input('Digite uma palavra: '))

for palavra in texto:
    if palavra in texto.lower():
        print(palavra, end='')