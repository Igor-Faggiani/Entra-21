import random

contadores = [0, 0, 0, 0, 0, 0]

for _ in range(100):
    resultado = random.randint(1, 6)
    contadores[resultado - 1] += 1

for valor, contador in enumerate(contadores):
    print(f"O valor {valor + 1} foi conseguido {contador} vezes.")