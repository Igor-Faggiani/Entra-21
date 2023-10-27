# identidade = []
# dicionario = {}
#
#
# def mostrar_menu() -> None:
#     """Exibe o menu da aplicação."""
#     print("""\n--- Gerenciamento de livros ---
# 1: Adicionar Livro
# 2: Remover Livro
# 3: Emprestar Livro
# 4: Devolver Livro
# 5: Listar Livros
# 6: Buscar Livro
# 7: Livros por Autor
# 8: Livros por Gênero
# 9: Livros Emprestados
# 10: Avaliar Livro
# 11: Obter Média das Avaliações
# 12: Sair
# """)
#
#
# def adicionar_livro(identificador: int, livro: str, autor: str, ano_publicacao: int, genero: str) -> None: # Case 1    """Adiciona um livro no sistema."""
#     if identificador in dicionario:
#         print("O livro já consta no sistema.")
#         return
#     for livro_info in dicionario.values():
#         if livro == livro_info['Título']:
#             print("O livro já consta no sistema.")
#             return
#     avaliacoes = []
#     status = input("Digite 'E' caso o livro esteja emprestado ou 'D' caso o livro esteja disponível: ").lower()
#     if status == "d" :
#         status = "Disponível"
#     elif status == "e" :
#         status = "Emprestado"
#     else:
#         print("Dado incorreto, tente novamente.")
#         return
#     dicionario[identificador] = {"Título": livro, "Autor": autor,
#                                  "Ano de Publicação": ano_publicacao, "Gênero": genero, "Avaliações": avaliacoes,
#                                  "Status": status}
#
#
# def remover_livro(identificador: int) -> None:  # Case 2
#     """Remove um livro da biblioteca usando o Id."""
#     if identificador in dicionario:
#         print(f"O livro: {dicionario[identificador]['Título']}, Id {dicionario[identificador]} foi removido")
#         del (dicionario[identificador])
#     else:
#         print(f"Id {dicionario[identificador]} não encontrado")
#
#
# def emprestar_livro(identificador: int) -> None:  # Case 3
#     """Faz o empréstimo de um livro"""
#     if identificador in dicionario:
#         if dicionario[identificador]['Status'] == "Emprestado":
#             print("O livro ja está emprestado.")
#         else:
#             dicionario[identificador]['Status'] = "Emprestado"
#             print(f"O livro {dicionario[identificador]['Título']} está agora emprestado. ")
#
#
# def devolver_livro(identificador: int) -> None:  # Case 4
#     """Faz a devolução de um livro"""
#     if identificador in dicionario:
#         if dicionario[identificador]['Status'] == "Disponível":
#             print("O livro já está disponível.")
#         else:
#             dicionario[identificador]['Status'] = "Disponível"
#             print(f"O livro {dicionario[identificador]['Título']} está agora disponível. ")
#
#
# def listar_livros() -> None:  # Case 5
#     """Lista todos os livros registrados e suas informações."""
#     print("\nLista de livros: ")
#     for identificador in dicionario:
#         print(
#             f"ID: {identificador} | Título: {dicionario[identificador]['Título']} | Autor: {dicionario[identificador]['Autor']} | "
#             f"Ano de publicação: {dicionario[identificador]['Ano de Publicação']} |"
#             f" Gênero: {dicionario[identificador]['Gênero']} | Avaliações: {', '.join(dicionario[identificador]['Avaliações'])} |"
#             f" Status: {dicionario[identificador]['Status']}")
#
#
# def buscar_livro(titulo: str) -> None:  # Case 6
#     """Exibe as informações de um livro."""
#     for i in dicionario:
#         if titulo in i.values():
#             print(
#                 f"Título: {dicionario[i]['Título']} | Autor: {dicionario[i]['Autor']} | "
#                 f"Ano de publicação: {dicionario[i]['Ano de Publicação']} |"
#                 f" Gênero: {dicionario[i]['Gênero']} | Avaliações: {dicionario[i]['Avaliações']} |"
#                 f" status: {dicionario[i]['Status']}")
#         else:
#             print("Livro não encontrado!")
#
#
# def livro_autor(autor: str) -> None:  # Case 7
#     """ Retorna uma lista de todos os livros de um determinado autor!"""
#     for i in dicionario:
#         if autor in i.values:
#             print(
#                 f"Título: {dicionario[i]['Título']} | Autor: {dicionario[i]['Autor']} | "
#                 f"Ano de publicação: {dicionario[i]['Ano de Publicação']} |"
#                 f" Gênero: {dicionario[i]['Gênero']} | Avaliações: {dicionario[i]['Avaliações']} |"
#                 f" Status: {dicionario[i]['Status']}")
#         else:
#             print("Autor não encontrado!")
#
#
# def genero_livro(genero: str) -> None:  # Case 8
#     """ Retorna uma lista de todos os livros de um determinado genero!"""
#     for i in dicionario:
#         if genero in i:
#             print(
#                 f"Título: {dicionario[i]['Título']} | Autor: {dicionario[i]['Autor']} | "
#                 f"Ano de publicação: {dicionario[i]['Ano de Publicação']} |"
#                 f" Gênero: {dicionario[i]['Gênero']} | Avaliações: {dicionario[i]['Avaliações']} |"
#                 f" status: {dicionario[i]['Status']}")
#         else:
#             print("gênero não encontrado!")
#
#
# def livros_emprestados() -> None:  # Case 9
#     """ Retorna uma lista de todos os livros emprestados"""
#     for i in dicionario:
#         if dicionario[i]["Status"] == "Emprestado":
#             print(f"Título: {dicionario[i]['Título']} | Autor: {dicionario[i]['Autor']} | "
#                   f"Ano de publicação: {dicionario[i]['Ano de Publicação']} | "
#                   f"Gênero: {dicionario[i]['Gênero']} | Avaliações: {dicionario[i]['Avaliações']} | "
#                   f"status: {dicionario[i]['Status']}")
#         else:
#             print("Não há livros emprestados.")
#
#
# def avaliar_livro(identificador: int) -> None:  # Case 10
#     """ Adiciona uma avaliação a um livro."""
#     if identificador in dicionario:
#         if dicionario[identificador]['Status'] == "Emprestado":
#             print("Não é possível avaliar um livro que está emprestado.")
#         else:
#             avaliacao = int(input("Informe a avaliação, de 1 a 5: "))
#             if avaliacao < 1 or avaliacao > 5:
#                 print("Valor incorreto, tente novamente.")
#             else:
#                 dicionario[identificador]['Avaliações'].append(avaliacao)
#     else:
#         print("Livro não encontrado!")
#
#
#
# def obter_media_avaliacoes(identificador: int) -> None:  # Case 11
#     """ Obtém a média de avaliação de um livro"""
#     if identificador in dicionario:
#         avaliacoes = dicionario[identificador]['Avaliações']
#         if not avaliacoes:
#             print("O livro ainda não foi avaliado.")
#         else:
#             soma = sum(avaliacoes)
#             media = soma / len(avaliacoes)
#             print(f"A média das avaliações do livro é {media:.2f}.")
#     else:
#         print("Id não encontrado no sistema.")
#
# # def obter_media_avaliacoes(identificador: int) -> None:  # Case 11
# #     """ Obtém a média de avaliação de um livro"""
# #     soma = 0
# #     cont = 0
# #     if identificador in dicionario:
# #         for nota in dicionario[identificador]['Status']:
# #             soma += int(nota)
# #             cont += 1
# #     else:
# #         print("Id não encontrado no sistema.")
# #         return
# #     media = soma / cont
# #     print(f"A média das avaliações do livro é {media}. ")
#
#
# # Menu para interação
# while True:
#     mostrar_menu()
#     opcao = input("Escolha uma opção: ")
#
#     match opcao:
#         case "1":
#             identificador = int(input("Informe o ID do livro.\nEle não pode já estar sendo utilizado, tem que ser um novo: "))
#             if identificador in identidade:
#                 print("O ID já está sendo utilizado, tente novamente.")
#                 continue
#             else:
#                 identidade.append(identificador)
#             livro = input("Digite o nome do Livro: ")
#             autor = input("Digite o Autor do livro: ")
#             ano_publicacao = int(input("Digite o ano de publicação do livro: "))
#             genero = input("Digite o gênero do livro: ")
#             adicionar_livro(identificador, livro, autor, ano_publicacao, genero)
#         case "2":
#             identificador = int(input("Digite o id do livro a ser removido: "))
#             remover_livro(identificador)
#         case "3":
#             identificador = int(input("Digite o id do livro a ser emprestado: "))
#             emprestar_livro(identificador)
#         case "4":
#             identificador = int(input("Digite o id do livro a ser devolvido: "))
#             devolver_livro(identificador)
#         case "5":
#             listar_livros()
#         case "6":
#             titulo = input("Digite o nome do livro: ")
#             buscar_livro(titulo)
#         case "7":
#             autor = input("Informe um autor: ")
#             livro_autor(autor)
#         case "8":
#             genero = input("Informe um gênero de livro: ")
#             genero_livro(genero)
#         case "9":
#             livros_emprestados()
#         case "10":
#             identificador = int(input("Informe o id do livro: "))
#             avaliar_livro(identificador)
#         case "11":
#             identificador = int(input("Informe o id do livro: "))
#             obter_media_avaliacoes(identificador)
#         case "12":
#             print("Encerrando.")
#             break
#         case _:
#             print("Opção inválida!")


import re

contas = {"nenhuma": {"status": "ativo"}}
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

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

def fazer_pedido():
    """Função para o cliente fazer o pedido"""
    pedido = []

    mostrar_menu()
    escolha = input("Digite o número do prato que deseja pedir (ou '0' para encerrar): ")

    if escolha == 0:
        break

    try:
        escolha = int(escolha)
            if escolha < 1 or escolha > len(cardapio):
                print("Opção inválida. Por favor, escolha um número válido.")
            else:
                pedido.append(cardapio[escolha - 1]['nome'])
                print(f"{cardapio[escolha - 1]['nome']} adicionado ao pedido.")
        except ValueError:
            print("Opção inválida. Por favor, digite um número.")

    return pedido


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


    while True:
        email = input("Digite o seu email: ")
        senha = input("Digite a senha: ")
        if not re.match(pattern, email):
            input("O Email é inválido! (Aperte Enter para continuar!)")
            continue
        if email in contas and contas[email]["senha"] == senha:
            input("Bem-vindo ao restaurante Casella!(Digite Enter para voltar ao menu principal!)")
            contas.update({"nenhuma": {"status": "desativado"}})
            contas.update({email: {"status": "ativado"}})
            break
        else:
            while True:
                resposta = input("O email não existe na base de dados, você deseja se registrar? (S/N)").strip().lower()
                if resposta == "s":
                    adicionar_login()
                    break
                elif resposta == "n":
                    input("Aprete Enter para voltar ao menu principal!")
                    break
                else:
                    input("Opção inválida!(Aprete Enter para digitar outra resposta!)")
                    continue
        break


def adicionar_login() -> None:
    """Adiciona o usuario"""
    while True:
        nome = input("Digite seu nome: ")
        email = input("Digite seu email: ")
        if not re.match(pattern, email):
            input("O Email é inválido! (Aperte Enter para continuar!)")
            continue

        elif email in contas:
            input("O email já existe! (Digite Enter para voltar ao menu!)")
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
                    contas.update({email: {"senha": senha, "status": "ativo"}})
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

def sair_usuario() -> None:
    input("Sair com sucesso! (Aperte Enter para voltar ao menu principal!)")
    for conta in contas:
        if contas[conta]["status"] == "ativado":
            contas.update({conta: {"status": "desativado"}})


while True:
    if contas["nenhuma"]["status"] == "ativado":
        print(f"Registre ou entre para personalização.")
    else:
        for conta in contas:
            if contas[conta]["status"] == "ativado":
                print(f"Seja Bem vindo, {contas[conta]['nome']}!")
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
            login_usuario()
        case 3:
            sair_usuario()
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
