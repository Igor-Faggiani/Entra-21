# Criação de uma lista
numeros = []

# Cadastrando elementos na lista
# for _ in range(5):
#     numeros.append(int(input("Digite um número: ")))

# Remover elementos da lista
frutas = ["abacate", "ameixa", "amora", "banana", "caqui", "ameixa"]

frutas.pop(-2)  # Índice
frutas.remove("abacate")
print(frutas)

# Editando elementos da lista
for indice, fruta in enumerate(frutas):
    if fruta == "ameixa":
        frutas[indice] = "maçã"

print(frutas)

print(frutas.index("maçã"))

#                  0    1   2   3
classificacoes = [100, 80, 70, 60]
for i, nota in enumerate(classificacoes):
    print(f"Nota: {nota} | Posição: {indice + 1}º lugar")

for classificacao in classificacoes:
    print(classificacao, end=" ")

print()


# Juntando duas listas
nomes = ["Ana", "Maria", "Pedro"]
notas = [10, 9, 8]

for nome, nota in zip(nomes, notas):
    print(f"Nome: {nome} | Nota: {nota}")

print(nomes, notas)

# Extender listas
nomes.extend(notas)
print(nomes)

# Desempacotar (*)
nomes_e_notas = [*nomes, *notas]
print(nomes_e_notas)
print(*nomes, sep=", ")

# List comprehension
frutas = ["abacaxi", "abacate", "banana", "tomate"]

nova_lista = [fruta for fruta in frutas if fruta[0] == "a"]
nova_lista = []
for fruta in frutas:
    if fruta[0] == "a":
        nova_lista.append("maçã")
    else:
        nova_lista.append(fruta)

print(nova_lista, frutas)

nomes = ["A", "B", "C"]
notas = [10, 9, 8]

resultados = [f"Nome: {nome} | Nota: {nota}" for nome, nota in zip(nomes, notas)]
print(resultados)

notas1 = [1, 2, 3]
notas2 = [1, 2, 3]

# Invertendo o vetor
notas1.reverse()
print(notas1)

print(notas2[::-1])
print(notas2)

# Ordenando vetor
letras = ["a", "d", "b"]
letras.sort(reverse=True)
print(letras)

'''
Faça um programa que leia e monte dois vetores de números inteiros com 3 números cada. Depois
de montados gere um terceiro vetor formado pela diferença dos dois vetores lidos, um quarto vetor
formado pela soma dos dois vetores lidos e por último um quinto vetor formado pela multiplicação
dos dois vetores lidos.
'''
vetor1 = []
vetor2 = []
vetor_diferenca = []
vetor_soma = []
vetor_multiplicacao = []

for i in range(3):
    vetor1.append(int(input(f"Digite o {i + 1}º valor do primeiro vetor: ")))
    vetor2.append(int(input(f"Digite o {i + 1}º valor do segundo vetor: ")))

    vetor_diferenca.append(vetor1[i] - vetor2[i])
    vetor_soma.append(vetor1[i] + vetor2[i])
    vetor_multiplicacao.append(vetor1[i] * vetor2[i])

print(f"""
Vetor 1: {vetor1}
Vetor 2: {vetor2}
Vetor diferença: {vetor_diferenca}
Vetor soma: {vetor_soma}
Vetor multiplicação: {vetor_multiplicacao}
""")

vetor1 = [int(input(f"Digite o {i + 1}º número do primeiro vetor: ")) for i in range(3)]
vetor2 = [int(input(f"Digite o {i + 1}º número do segundo vetor: ")) for i in range(3)]

#            (     valor   ) (                 for in iterable         ) ( if condicao )
vetor_soma = [valor1 + valor2 for valor1, valor2 in zip(vetor1, vetor2)]
vetor_subtracao = [valor1 - valor2 for valor1, valor2 in zip(vetor1, vetor2)]
vetor_multiplicacao = [valor1 * valor2 for valor1, valor2 in zip(vetor1, vetor2)]

print(f"""
Vetor 1: {vetor1}
Vetor 2: {vetor2}
Vetor diferença: {vetor_subtracao}
Vetor soma: {vetor_soma}
Vetor multiplicação: {vetor_multiplicacao}
""")

# 0 1 2 3 4 5 6 7 8 9 10
pares = [numero for numero in range(11) if numero % 2 == 0]  # [0, 2, 4, 6, 8, 10]
print(pares)

impares = [f"{numero} é ímpar" for numero in "12345"]
print(impares)

nome = "Willium"
if "a" in nome:
    print("Tem a")