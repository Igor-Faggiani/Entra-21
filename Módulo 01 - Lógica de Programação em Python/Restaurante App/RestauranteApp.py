contas = {"nenhuma": {"status": "ativa"}}

def escolher_forma_pagamento():
    while True:
        print("\nForma de Pagamento:")
        print("1. Dinheiro")
        print("2. Cartão")
        forma_pagamento = input("Escolha a forma de pagamento (1 para Dinheiro, 2 para Cartão): ")

        if forma_pagamento == '1':
            return 'Dinheiro'
        elif forma_pagamento == '2':
            return 'Cartão'
        else:
            print("Opção inválida. Por favor, escolha 1 para Dinheiro ou 2 para Cartão.")


def finalizar_pedido(pedido):
    print("\nResumo do Pedido:")
    for prato in pedido:
        print(f"{prato['nome']} - R$ {prato['preco']:.2f}")

    total_pedido = calcular_total_pedido(pedido)
    print(f"Total a pagar: R$ {total_pedido:.2f}")

    forma_pagamento = escolher_forma_pagamento()
    print(f"Forma de Pagamento: {forma_pagamento}")

    confirmacao = input("Confirma o pedido (S para Sim, N para Não)? ").strip().lower()
    if confirmacao == 's':
        print("Pedido confirmado! Obrigado por escolher o Restaurante Pizzaria Bella.")
    else:
        print("Pedido cancelado. Seu pedido não foi finalizado.")


def calcular_total_pedido(pedido):
    total = sum(prato['preco'] for prato in pedido)
    return total


def login_usuario() -> None:
    """Login do Usuario"""
    email = input("Digite o seu email: ")
    senha = input("Digite a senha: ")

    if email in contas and contas[email]["senha"] == senha:
        print("Bem-vindo ao restaurante Casella!")
    else:
        print("Login não existe na base de dados!")


def adicionar_login() -> None:
    """Adiciona o usuario"""
    while True:
        nome = input("Digite seu nome: ")
        email = input("Digite seu email: ")

        if email in contas:
            print("O email já existe")
            continue
        else:
            contas.update({email: {"nome": nome}})
            while True:
                senha = input("Digite uma senha: ")
                confirma_senha = input("Digite a senha novamente: ")

                if senha != confirma_senha:
                    input("As senhas não correspondem!")
                    continue
                else:
                    contas.update({email: {"senha": senha}})
                    contas.update({"nenhuma": {"status": "desativado"}})
                    input("Conta cadastrada com sucesso! (Digite Enter para voltar ao menu principal)")
                    break
        break


cardapio_resumido = {1: {"nome": "Pizza Margherita"},
                     2: {"nome": "Pizza Peperoni"},
                     3: {"nome": "Pizza de Calabresa"},
                     4: {"nome": "Pizza Quatro Queijos"},
                     5: {"nome": "Pizza Frango com Catupiry"},
                     6: {"nome": "Pizza Vegetariana"},
                     7: {"nome": "Pizza Rúcula com Tomate Seco"},
                     8: {"nome": "Pizza Havaiana"},
                     9: {"nome": "Pizza Bacon com Ovo"},
                     10: {"nome": "Pizza Mexicana"}}


def avaliacao_pizza():
    while True:
        print("""1: Pizza Margherita,
                 2: Pizza Peperoni
                 3: Pizza de Calabresa
                 4: Pizza Quatro Queijos
                 5: Pizza Frango com Catupiry
                 6: Pizza Vegetariana
                 7: Pizza Rúcula com Tomate Seco
                 8: Pizza Havaiana
                 9: Pizza Bacon com Ovo
                 10: Pizza Mexicana
                 0:  Sair
        """)
        avaliar_id = int(input("Qual prato do cardápio deseja avaliar? "))
        if avaliar_id == 0:
            mostrar_menu()
        else:
            while True:
                if avaliar_id not in cardapio_resumido.keys():
                    print("O prato não existe no restaurante")
                    break
                else:
                    avaliacao = int(input("Qual a nota da avaliação, ela deve ser entre 1 - 5? "))
                    if avaliacao > 0 and avaliacao < 6:
                        if "avaliacoes" in cardapio_resumido[avaliar_id]:
                            cardapio_resumido[avaliar_id]["avaliacoes"].append(avaliacao)
                            print(cardapio_resumido[avaliar_id]["nome"], cardapio_resumido[avaliar_id]["avaliacoes"])
                            break
                        else:
                            cardapio_resumido[avaliar_id].update({"avaliacoes": [avaliacao]})
                            print(cardapio_resumido[avaliar_id]["nome"], cardapio_resumido[avaliar_id]["avaliacoes"])
                            break
                    else:
                        print("Valor da avaliação inválida")


def media_avaliacoes():
    while True:
        print("""1: Pizza Margherita,
                 2: Pizza Peperoni
                 3: Pizza de Calabresa
                 4: Pizza Quatro Queijos
                 5: Pizza Frango com Catupiry
                 6: Pizza Vegetariana
                 7: Pizza Rúcula com Tomate Seco
                 8: Pizza Havaiana
                 9: Pizza Bacon com Ovo
                 10: Pizza Mexicana
                 0:  Sair
        """)
        avaliar_id = int(input("Qual prato do cardápio deseja avaliar? "))
        if avaliar_id == 0:
            mostrar_menu()
        else:
            if avaliar_id in cardapio_resumido:
                if 'avaliacoes' in cardapio_resumido[avaliar_id]:
                    avaliacoes = cardapio_resumido[avaliar_id]["avaliacoes"]
                    if avaliacoes:
                        media = sum(avaliacoes) / len(avaliacoes)
                        return print(f'A media das avaliações dessa pizza é de {media:.2f} estrelas')
                    else:
                        return "Esta pizza ainda não foi avaliada."
                else:
                    print("Essa pizza ainda não foi avaliada")
            else:
                return "Essa pizza não existe no restaurante"


while True:
    if contas["nenhuma"]["status"] == "ativado":
        pass
    print("""
    1) Registrar uma conta
    2) Entrar na conta
    3) Sair da conta
    4) Comidas
    5) Bebidas
    6) Avaliações
    7) Suporte ao cliente
    8) Reservar mesa (EM BREVE)
    9) Reservar para eventos (EM BREVE)
    10) Sair do app
""")
    opcao = int(input("Digite a opção desejada: "))
    match opcao:
        case 1:
            adicionar_login()
        case 2:
            # Função para entrar em uma conta
            pass
        case 3:
            # Função para sair da conta
            pass
        case 4:
            # Função para abrir o cardápio de comidas
            pass
        case 5:
            # Função para abrir o cardápio de bebidas
            pass
        case 6:
            avaliar = input("Você deseja avaliar um pedido? (S/N) ")
            if avaliar == S:
                avaliacao_pizza()
            else:
                acessar_media = input("Você deseja ver qual a média das avaliações de um prato? (S/N)")
                if acessar_media == S:
                    media_avaliacoes()
                else:
                    break
        case 7:
            # Função do suporte ao cliente
            pass
        case 8:
            input("Sentimos muito, mas a opção de reservar uma mesa ainda não está abilitada (Aperte Enter para voltar"
                  " ao menu principal)")
        case 9:
            input("Sentimos muito, mas a opção de reservar para eventos ainda não está abilitada (Aperte Enter para"
                  " voltar ao menu principal)")
        case 10:
            input("Espero que tenha gostado do nosso aplicativo! (Aperte Enter para sair)")
            break
        case _:
            input("Opção Inválida! (Aperte Enter para voltar ao menu principal)")
