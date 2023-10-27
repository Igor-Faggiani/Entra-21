horas = int(input('Digite a hora: '))
minutos = int(input('Digite os minutos: '))
segundos = int(input('Digite os segundos: '))
conv_minutos = minutos + (horas * 60)
conv_segundos = segundos + (conv_minutos * 60)
print(f'Convertendo os valores para segundos fica: {conv_segundos} segundos!')



