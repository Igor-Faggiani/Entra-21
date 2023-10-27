pessoas_maiores = []
pessoas_menores = []

quantidade_pessoas = int(input("Quantas pessoas serão cadastradas? "))

# Ler os dados das pessoas e classifir
for i in range(quantidade_pessoas):
    nome = input(f"Digite o nome da pessoa {i + 1}: ")
    cpf = input(f"Digite o CPF da pessoa {i + 1}: ")
    idade = int(input(f"Digite a idade da pessoa {i + 1}: "))

    pessoa = {"Nome": nome, "CPF": cpf, "Idade": idade}

    if idade >= 18:
        pessoas_maiores.append(pessoa)
    else:
        pessoas_menores.append(pessoa)

# Exibir as pessoas maiores de idade
print("\nPessoas Maiores de Idade:")
for pessoa in pessoas_maiores:
    print(f"Nome: {pessoa['Nome']} | CPF: {pessoa['CPF']} | Idade: {pessoa['Idade']}")

# Exibir as pessoas menores de idade
print("\nPessoas Menores de Idade:")
for pessoa in pessoas_menores:
    print(f"Nome: {pessoa['Nome']} | CPF: {pessoa['CPF']} | Idade: {pessoa['Idade']}")
