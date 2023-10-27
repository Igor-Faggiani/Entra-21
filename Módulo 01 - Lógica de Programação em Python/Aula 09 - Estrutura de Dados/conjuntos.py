"""
Conjuntos (Sets) são uma coleção que possuem as seguintes características:

- Não ordenado
- Elementos únicos
- Mutável
- Não indexável
"""

# Criando um conjunto
conjunto = {1, 2, 3}
print(type(conjunto))

# Transformar uma lista em um conjunto
lista = [1, 2, 3, 4, 4, 5, 6]
lista = list(set(lista))
print(lista)

# Adicionar elementos em um conjunto
conjunto = {1, 2, 3}
conjunto.add(5)
print(conjunto)

# Removendo elementos
conjunto.remove(2)
print(conjunto)

conjunto.discard(2)  # Não levanta erro
print(conjunto)

conjunto.pop()
print(conjunto)

conjunto.clear()

print(conjunto)

# Unindo conjuntos
a = {1, 2, 3}
b = {3, 5, 6}

print(a | b)

# Intersecção dos conjuntos
print(a & b)

# Diferença dos conjuntos
print(b - a)

# Diferença simétrica
print(a ^ b)

if 1 in a:
    print("Existe o número 1 no conjunto a")