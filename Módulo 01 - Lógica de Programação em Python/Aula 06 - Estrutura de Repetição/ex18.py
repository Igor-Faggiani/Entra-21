palavra = input('Digite uma palavra: ')

inicio = 0
fim = len(palavra) - 1

#Variavel para saber se é palindromo:
e_palindromo = True

#Verificar se a palavra é palindromo:
while inicio < fim:
    if palavra[inicio] != palavra[fim]:
        e_palindromo = False
        break
    inicio += 1
    fim -= 1

#Exibir o resultado:
if e_palindromo:
    print('A palavra é um palíndromo!')
else:
    print('A palavra não é um palíndromo!')
