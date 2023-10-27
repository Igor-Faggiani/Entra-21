valor_x = int(input('Digite um número: '))
valor_n = int(input('Digite a potência: '))

resultado = 1

for _ in range(valor_n):
    resultado *= valor_x

print(resultado)