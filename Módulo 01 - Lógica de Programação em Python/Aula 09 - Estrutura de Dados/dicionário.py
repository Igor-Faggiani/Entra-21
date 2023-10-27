"""
Dicionário é uma estrutura de dados baseada em chave-valor (HashMap).
"""
# Criando um dicionário
dicionario = {"chave1": "valor1", "chave2": 10}
print(type(dicionario))

pessoa = {
    "nome": "Ana",
    "idade": 26,
    "cor_cabelo": "preto",
}

# Acessando os dados
print(pessoa["nome"])

print(pessoa.get("nomea", "Valor não existe"))

# Adicionando valores no dicionário
pessoa["peso"] = 60
print(pessoa)

pessoa.update({"altura": 1.65})
print(pessoa)

# Atualizando o valor do dicionário
pessoa["nome"] = "Ana Beatriz"
print(pessoa)

# Verificando a existência de uma chave
if "nome" in pessoa:
    print("A chave nome existe dentro do dicionário pessoa.")

# Iterar pelas chaves do dicionário
for chave in pessoa:
    print(chave)

# Iterar pelos valores do dicionário
for valor in pessoa.values():
    print(valor)

# Iterar pelos itens do dicionário
for chave, valor in pessoa.items():
    print(chave, valor)

# Lista com as chaves
print(pessoa.keys())

# Dicionários aninhados
pessoas = {
    "João": {"idade": 30, "cidade": "Rio de Janeiro"},
    "Maria": {"idade": 30, "cidade": "São Paulo"}
}

print(pessoas["João"]["idade"])

# Remover elemento do dicionário
del pessoas["João"]

print(pessoas)

"""
Escreva um programa que dado um valor inteiro de reais, mostre a quantidade de notas de:
1 real
2 reais
5 reais
10 reais
20 reais
50 reais
100 reais
200 reais
"""

notas = {
    200: 0,
    100: 0,
    50: 0,
    20: 0,
    10: 0,
    5: 0,
    2: 0,
    1: 0
}

valor_original = float(input("Digite o valor do saque: "))
valor = valor_original

for nota in notas:
    if valor >= nota:
        quantidade_notas = valor // nota
        notas[nota] = quantidade_notas
        valor -= quantidade_notas * nota

print(f"Valor do saque: R$ {valor_original:.2f}")
for nota, quantidade in notas.items():
    print(f"Nota de R$ {nota}: {quantidade}")

"""
Exemplo 2)

Faça um programa que leia o nome e as três notas de três alunos.
Ao final, mostre um relatório com o nome, as notas e a média de cada aluno.
"""
alunos = []

for i in range(3):
    nome = input(f"Digite o nome do {i + 1}º aluno")
    notas = [float(input(f"Digite a {j + 1}ª nota do {nome}: ")) for j in range(3)]
    media = sum(notas) / len(notas)

    alunos.append({"nome": nome, "notas": notas, "media": media})

for aluno in alunos:
    print(f"""Aluno: {aluno["nome"]}
Notas: {", ".join(map(str, aluno["notas"]))}
Média: {aluno["media"]}
""")

aluno_procurado = input("Digite o nome do aluno")

for aluno in alunos:
    if aluno_procurado == aluno["nome"]:
        print(aluno)
        break