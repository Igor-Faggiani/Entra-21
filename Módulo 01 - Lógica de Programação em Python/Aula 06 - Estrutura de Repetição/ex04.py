soma = 0
while True:
    numero = int(input('Digite um número: '))

    if numero <= 0:
        break
    
    soma += numero

print(f'A soma dos numeros é: {soma}')