"""
Lambdas são pequenas funções anônimas
"""
quadrado = lambda x: x ** 2
multiplicacao = lambda x, y: x * y

print(quadrado(5))
print(multiplicacao(10, 5))

# Exemplo prático da utilização de lambdas
pessoas = [
    {'nome': 'Ana', 'idade': 35},
    {'nome': 'Bob', 'idade': 25},
    {'nome': 'Eva', 'idade': 30}
]

# Ordenar as pessoas pela idade
pessoas_ordenadas = sorted(pessoas, key=lambda pessoa: pessoa["idade"])
print(pessoas_ordenadas)