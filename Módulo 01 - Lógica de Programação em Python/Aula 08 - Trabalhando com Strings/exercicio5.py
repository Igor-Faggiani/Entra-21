spam = False

while True:
    palavras = input('Digite uma palavra ou frase: ')

    if 'jequeti' in palavras.lower() or 'curso de python' in palavras.lower():
        print('Esse texto é spam!')
    else:
        print('Esse texto não é spam!')




