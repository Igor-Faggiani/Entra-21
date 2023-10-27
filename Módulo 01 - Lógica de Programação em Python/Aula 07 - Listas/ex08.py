lista = []
vetor_x = 0
vetor_y = 0
for i in range(2):
    numeros = int(input('Digite um número de 1 a 9: '))
    lista.append(numeros)

valor_x = None
valor_y = None

while True:
    valor_x = int(input('Digite um valor de 1 a 9 para X: '))
    if valor_x in lista:
        vetor_x += valor_x
        break
    else:
        print('O valor é inválido!')

while True:
    valor_y = int(input('Digite um valor de 1 a 9 para Y: '))
    if valor_y in lista:
        vetor_y += valor_y
        break
    else:
        print('O valor é inválido!')

print(f'A soma entre {valor_x} e {valor_y} é: {valor_x + valor_y}')
