lista_numeros = []
numeros_pares = []
cal_soma = 0
divisor = 3
for i in range(3):
    numeros = int(input('Digite um número: '))
    lista_numeros.append((numeros))

for c in lista_numeros:
    if c % 2 == 0:
        numeros_pares.append(c)

for s in numeros_pares:
    cal_soma += s

resultado = cal_soma / divisor

print(f'A média dos números pares é de: {resultado}')

