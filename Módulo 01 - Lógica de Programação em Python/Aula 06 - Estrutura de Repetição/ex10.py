maior_numero = 0
menor_numero = 0
# 0 1 2 3 4
for i in range(5):
    numero = int(input('Digite um número: '))
    if i == 0:
        maior_numero = numero
        menor_numero = numero

    if numero < menor_numero:
        menor_numero = numero

    if numero > maior_numero:
        maior_numero = numero

print(f'O maior numero é: {maior_numero}')
print(f'O menor numero é: {menor_numero}')