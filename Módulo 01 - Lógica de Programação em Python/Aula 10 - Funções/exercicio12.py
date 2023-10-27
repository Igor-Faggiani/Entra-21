def calcular_media(lista):
    """
    Calcula a média de uma lista de números.

    Args:
        lista (list): Uma lista de números.

    Returns:
        float: A média dos números na lista.
    """
    if not lista:
        return 0.0  # Retorna 0 se a lista estiver vazia
    soma = sum(lista)
    media = soma / len(lista)
    return media


numeros = [10, 20, 30, 40, 50]
media = calcular_media(numeros)
print(media)