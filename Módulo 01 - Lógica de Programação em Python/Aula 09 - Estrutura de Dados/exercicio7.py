matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0 ,3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f"Digite o valor para [{linha}, {coluna}]: "))

for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end="")
    print()

valor_x = int(input("Digite um numero: "))

encontrado = False

for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] == valor_x:
            encontrado = True
            print(f"O valor {valor_x} foi encontrado na coordenada: [{l}, {c}].")
            break

if not encontrado:
    print("O valor não foi encontrado")