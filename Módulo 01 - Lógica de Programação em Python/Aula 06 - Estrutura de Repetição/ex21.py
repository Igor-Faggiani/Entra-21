numero = int(input('Digite um numero positivo: '))

for i in range(2, numero):
    if numero % i == 0:
        print('O número não é primo!')
        break
else:
    print('O número é primo!')