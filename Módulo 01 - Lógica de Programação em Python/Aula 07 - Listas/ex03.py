numeros = []

for i in range(1, 6):
    numero = int(input(f'Digite o número {i}: '))
    numeros.append(numero)
    numeros.sort()

if numeros[0]:
    print(f'O menor número é: {numeros[0]}')

if numeros[4]:
    print(f'O maior numero é: {numeros[4]}')
