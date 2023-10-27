lista = []
media = 3
soma = 0

for i in range(3):
    notas = float(input('Digite sua nota: '))
    lista.append(notas)

for s in lista:
    soma += s
    media = soma / 3

print(f'Notas: {lista}')
print(f'Media: {media:.2f}')

if media >= 7:
    print('APROVADO!')
else:
    print('REPROVADO!')