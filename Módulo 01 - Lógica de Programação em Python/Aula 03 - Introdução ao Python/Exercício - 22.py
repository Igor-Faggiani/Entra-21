nome_livro = input('Digite o nome do Livro: ')
tempo_medio = int(input('Digite o tempo médio de para ler uma página (em segundos): '))
tempo_diario = int(input('Digite o tempo médio de leitura diária (em segundos): '))
quantidade_paginas = int(input('Digite a quantidade de páginas do livro: '))

paginas_por_dia = tempo_diario / tempo_medio
horas_necessarias = (quantidade_paginas * tempo_medio) / 3600
dias_necessarios = (quantidade_paginas * tempo_diario) / 3600
print(dias_necessarios)
print(horas_necessarias)
print(paginas_por_dia)