lista = [1, 1, 1, 2, 3, 3, 4, 4, 4, 4]

comprimida = []
i = 0

while i < len(lista):
    elemento = lista[i]
    contagem = 1

    while i + 1 < len(lista) and lista[i] == lista[i + 1]:
        contagem += 1
        i += 1

    if contagem > 1:
        comprimida.append((elemento, contagem))
    else:
        comprimida.append(elemento)

    i += 1

print(comprimida)