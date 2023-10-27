matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
contador = 0

#Adicionar valor na matriz
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input("Digite um número: "))

#Estrutura de repetição para mostrar a matriz
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end=" ")
    print()

#Estrutura de repetição para mostrar quantos valores maior que 10
for l in range(0 ,3):
    for c in range(0, 3):
        if matriz[l][c] >= 10:
            contador += 1

print(f'A matriz possui {contador} numeros maiores que 10.')
