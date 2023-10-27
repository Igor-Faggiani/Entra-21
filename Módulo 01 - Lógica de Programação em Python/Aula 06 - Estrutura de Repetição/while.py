#Solicitar um número até o usuário digitar um numero negativo. Fazer a soma dos números digitados.
soma = 0
while True:
    numero = int(input('Digite um número: '))

    if numero <= 0:
        break

    soma += numero

print(f'A soma dos números é: {soma}')

print()

#Mostrar todos os números pares de 0 a 100 utilizando while:
i = 0
while i <= 100:
    i += 1

    if 1 % 2 != 0:
        continue

    print(i, end=" ")