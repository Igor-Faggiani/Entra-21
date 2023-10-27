"""
Escreva um programa para armazenar uma agenda de telefones em um dicionário. Cada pessoa pode ter um ou mais telefones e
a chave do dicionário é o nome da pessoa. Seu programa deve ter as seguintes funções:

* Adicionar contato: acrescenta um novo nome na agenda com um ou mais telefones.
* Adicionar telefone: acrescenta um novo telefone em um nome já existente na agenda. Caso o nome não exista na agenda,
você deve perguntar se a pessoa deseja incluí-lo.
* Excluir telefone: remove o telefone de uma pessoa que já está cadastrada na agenda.
* Excluir contato: remove o nome de uma pessoa da agenda.
* Consultar contato: obtém as informações de contato de uma pessoa pelo nome.
* Listar contatos: listar todos os contatos (nome e telefones) presentes na agenda.
"""
from typing import List

agenda = {}


def mostrar_menu() -> None:
    """Exibe o menu da aplicação."""
    print("""\n--- Agenda Telefônica ---
1: Adicionar contato
2: Adicionar telefone
3: Excluir telefone
4: Excluir contato
5: Consultar contato
6: Listar contatos
7: Sair
""")


def adicionar_contato(nome: str, telefones: List[str]) -> None:
    """Adiciona um contato na agenda."""
    agenda[nome] = telefones


def adicionar_telefone(nome: str, telefone: str) -> None:
    """Adiciona um telefone a um contato na agenda."""
    if nome in agenda:
        agenda[nome].append(telefone)
    else:
        resposta = input(f"O nome {nome} não está na agenda. Deseja incluí-lo? (s/n) ")
        if resposta.lower() == 's':
            agenda[nome] = [telefone]


def excluir_telefone(nome: str) -> None:
    """Remove um telefone de um contato na agenda."""
    if nome in agenda:
        for indice, telefone in enumerate(agenda[nome]):
            print(f"{indice + 1}) {telefone}")
        indice_telefone = int(input("Selecione o telefone a ser removido: ")) - 1

        if indice_telefone not in range(len(agenda[nome])):
            print("O índice selecionado não existe")
        else:
            agenda[nome].pop(indice_telefone - 1)
    else:
        print("Nome não encontrado.")


def excluir_contato(nome: str) -> None:
    """Remove um contato da agenda."""
    if nome in agenda:
        del agenda[nome]
    else:
        print("Nome não encontrado")


def consultar_contato(nome: str) -> None:
    """Exibe as informações de um contato."""
    if nome in agenda:
        print(f"Contato: {nome} | Telefones: {', '.join(agenda[nome])}")
    else:
        print("Nome não encontrado")


def listar_contatos() -> None:
    """Exibe todos os contatos na agenda."""
    for nome, telefones in agenda.items():
        print(f"Contato: {nome} | Contatos: {', '.join(telefones)}")


# Menu para interação
while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            nome = input("Digite o nome do contato: ")
            telefones = input("Digite os telefones separados por vírgula: ").split(',')
            adicionar_contato(nome, telefones)
        case "2":
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o novo telefone: ")
            adicionar_telefone(nome, telefone)
        case "3":
            nome = input("Digite o nome do contato: ")
            excluir_telefone(nome)
        case "4":
            nome = input("Digite o nome do contato a ser removido: ")
            excluir_contato(nome)
        case "5":
            nome = input("Digite o nome do contato: ")
            consultar_contato(nome)
        case "6":
            listar_contatos()
        case "7":
            break
        case _:
            print("Opção inválida!")