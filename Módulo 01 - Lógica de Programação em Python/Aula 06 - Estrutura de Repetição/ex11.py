import random

numero_random = random.randint(1, 101)

while True:
    resposta = int(input('Digite um número: '))

    if resposta > numero_random:
        print('MAIOR')
    elif resposta < numero_random:
            print('MENOR')
    elif resposta == numero_random:
        print('Você acertou!')
        break