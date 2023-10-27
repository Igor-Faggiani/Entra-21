# Inicializar o tabuleiro
tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

jogador_atual = "X"
rodada = 1

while True:
    print(f"Rodada {rodada}")

    # Imprimir o tabuleiro
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

    # Solicitar a posição do jogador atual
    while True:
        linha = int(input(f"Jogador {jogador_atual}, escolha a linha (0, 1 ou 2): "))
        coluna = int(input(f"Jogador {jogador_atual}, escolha a coluna (0, 1 ou 2): "))

        if tabuleiro[linha][coluna] == " ":
            break
        else:
            print("Posição já está ocupada. Tente novamente.")

    tabuleiro[linha][coluna] = jogador_atual

    # Verificar se o jogador atual venceu
    # Verificar linhas
    if tabuleiro[linha][0] == tabuleiro[linha][1] == tabuleiro[linha][2] == jogador_atual:
        print(f"O jogador {jogador_atual} venceu!")
        break
    # Verificar colunas
    if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] == jogador_atual:
        print(f"O jogador {jogador_atual} venceu!")
        break
    # Verificar diagonais
    if linha == coluna and tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador_atual:
        print(f"O jogador {jogador_atual} venceu!")
        break
    if linha + coluna == 2 and tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador_atual:
        print(f"O jogador {jogador_atual} venceu!")
        break

    # Verificar empate
    if rodada == 9:
        for linha in tabuleiro:
            print(" | ".join(linha))
            print("-" * 9)
        print("O jogo empatou!")
        break

    # Alternar o jogador atual
    jogador_atual = "O" if jogador_atual == "X" else "X"
    rodada += 1
