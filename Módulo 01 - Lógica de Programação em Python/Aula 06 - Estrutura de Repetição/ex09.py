valor_inicial = int(input('Digite o valor inicial: '))
valor_final = int(input('Digite o valor final: '))

tem_numeros_pares = False

for i in range(valor_inicial, valor_final + 1):

    if i % 2 == 0:
        print(i)
        tem_numeros_pares = True

    if not tem_numeros_pares:
        print('Não há numeros pares no intervalo')
