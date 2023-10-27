"""
Em python nós podemos utilizar laços de repetição FOR para percorrer os elementos de um iterable
"""

#Criando uma Range:
print(range(10))

#Como saber se um método é iterable:
print(hasattr(range(10), "__iter__"))

#Utilizando o FOR para percorrer um RANGE:
#range(10) -> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
for i in range(10):
    print(i, end= " ") #O {end = " "} Mostra o print na mesma linha;
print()

#Mostra a lista de 1 -> 9
for i in range(1, 10):
    print(i, end= " ")

print()

#mostra a lista pulando 2 numeros
for i in range(1, 10, 2):
    print(i, end= " ")

print()

#Percorre Inversamente:
for i in range(10, 0, -1):
    print(i, end= " ")

print()

#Mostrar a quantidade de vezes que o código repetiu:
for i in range(1, 11):
    print(f'O código repetiu pela {i + 1} vez!')