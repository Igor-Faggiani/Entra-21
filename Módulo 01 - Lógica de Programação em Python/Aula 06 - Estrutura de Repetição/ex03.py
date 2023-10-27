'''
3. Escreva um programa que solicite ao usuário um número inteiro positivo
e exiba a tabuada desse número de 1 a 10 utilizando um loop for.
'''

numero = int(input('Digite um número inteiro positivo: '))

if numero <= 0:
    print('O número deve ser positivo!')
else:
    for i in range(1, 11):
        resultado = numero * i
        print(f'{numero} x {i} = {resultado}')
