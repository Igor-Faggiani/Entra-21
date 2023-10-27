numero_degraus = int(input('Digite o número de degraus: '))
degraus = '_'
for i in range(1, numero_degraus + 1):
    espacos = ' ' * (numero_degraus - i)
    degraus * i
    print(espacos + degraus)
