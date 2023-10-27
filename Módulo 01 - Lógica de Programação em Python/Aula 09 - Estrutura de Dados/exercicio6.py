tamanho = int(input("Digite o tamanho da Matriz I: "))

# matriz_identidade = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

matriz_identidade = []

for i in range(tamanho):
    linha = []
    for j in range(tamanho):
        if i == j:
            linha.append(1)
        else:
            linha.append(0)
    matriz_identidade.append(linha)

for linha in matriz_identidade:
    print(linha)