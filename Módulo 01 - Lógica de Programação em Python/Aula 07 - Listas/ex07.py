lista = []
tem_duplicata = False

for i in range(5):
    numeros = int(input('Digite um número: '))
    lista.append(numeros)

for j in range(len(lista)):
    for d in range(j + 1, len(lista)):
        if lista[j] == lista[d]:
            tem_duplicata = True
            break

if tem_duplicata:
    print('A lista contém Duplicata')
else:
    print(f'{lista}')