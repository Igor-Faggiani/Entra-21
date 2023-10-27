"""
 Faça um programa que então leia uma string e a imprima.
 Caso o valor digitado não seja um valor textual (ex.: 12345), uma mensagem deve ser
 mostrada para o usuário e o valor deve continuar sendo solicitado até que o mesmo seja válido.
"""

while True:
    nome = input('Digite uma palavra: ')
    if nome.isalpha():
        print(nome)
        break
    else:
        print('Apenas letras são válidas!')