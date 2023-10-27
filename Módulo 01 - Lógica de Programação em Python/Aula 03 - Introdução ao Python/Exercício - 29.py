"""
Escreva um algoritmo que leia um número de três dígitos e mostre ele na ordem inversa.
"""

numero = int(input('Digite um número de 3 digitos: '))

digito1 = numero % 10
digito2 = (numero // 10) % 10
digito3 = numero // 100

numero_invertido = digito1 * 100 + digito2 * 10 + digito3

print(f'O numero {numero} invertido fica: {numero_invertido}')