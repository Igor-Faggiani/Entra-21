time_a = int(input('Quandidade de gols do time A: '))
time_b = int(input('Quantidade de gols do time B: '))

if time_a > time_b:
    print('Vitória do time A!')
elif time_a < time_b:
    print('Vitória do time B!')
else:
    print('Jogo empatado!')
