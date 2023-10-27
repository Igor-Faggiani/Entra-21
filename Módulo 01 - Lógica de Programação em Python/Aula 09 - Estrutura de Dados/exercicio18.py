agenda = {}


# Menu para interação
while True:
    print("""
--- Agenda Telefônica ---
1: Adicionar contato
2: Adicionar telefone
3: Excluir telefone
4: Excluir contato
5: Consultar contato
6: Listar contatos
7: Sair""")

    opcao = input("Digite a opção desejada: ")

    match opcao:
        case "1":
            nome = input("Digite o nome do contato: ")
            telefones = input("Digite os telefones separados por vírgula: ").split(",")  # 47 9 8408-8520,47 9 8409-8520 -> ["47 9 8408-8520", "47 9 8409-8520"]
            agenda[nome] = telefones
        case "2":
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o novo telefone: ")
            if nome in agenda:
                agenda[nome].append(telefone)
            else:
                resposta = input(f"O nome {nome} não está na agenda. Deseja incluí-lo? (s/n): ").lower()
                if resposta == "s":
                    agenda[nome] = telefone
        case "3":
            nome = input("Digite o nome do contato: ")
            if nome in agenda:
                for indice, telefone in enumerate(agenda[nome]):
                    print(f"{indice + 1}) {telefone}")

                #    0         1        2
                # ["99999", "99999", "777777"]
                # 3)
                indice_telefone = int(input("Selecione o telefone a ser removido: ")) - 1

                if indice_telefone not in range(len(agenda[nome])):
                    print("O índice selecionado não existe.")
                else:
                    agenda[nome].pop(indice_telefone)
            else:
                print("Nome não foi encontrado na agenda.")
        case "4":
            nome = input("Digite o nome do contato: ")
            if nome in agenda:
                del agenda[nome]
            else:
                print("Nome não foi encontrado na agenda.")
        case "5":
            nome = input("Digite o nome do contato: ")
            if nome in agenda:
                print(f"Contato: {nome} | Telefones: {', '.join(agenda[nome])}")
            else:
                print("Nome não foi encontrado na agenda.")
        case "6":
            for nome, telefones in agenda.items():
                print(f"Contato: {nome} | Telefones: {', '.join(agenda[nome])}")
        case "7":
            break
        case _:
            print("Opção inválida")
