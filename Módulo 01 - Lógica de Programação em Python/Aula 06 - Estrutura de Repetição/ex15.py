# Inicializar variáveis para armazenar a média da turma
soma_medias = 0

# Loop para ler os dados de 5 alunos
for i in range(1, 3):
    print(f"--- Aluno {i} ---")
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    # Calcular a média do aluno
    media_aluno = (nota1 + nota2 + nota3) / 3
    soma_medias += media_aluno

    # Exibir a média do aluno
    print(f"A média de {nome} é: {media_aluno:.2f}\n")

# Calcular a média da turma
media_turma = soma_medias / 5

# Exibir a média da turma
print(f"A média da turma é: {media_turma:.2f}")

