aluno = 0
media = 0

for i in range(1, 3):
        nota = 0
        aluno += 1
        alunos = input(f'Digite o nome do {aluno}º aluno: ')


        for y in range(1, 4):
            nota += 1
            notas = float(input(f'Digite a {nota}ª nota do {alunos}: '))
            media += notas / 3
        print(f'ALUNO: {alunos} | MÉDIA: {media/2}')
