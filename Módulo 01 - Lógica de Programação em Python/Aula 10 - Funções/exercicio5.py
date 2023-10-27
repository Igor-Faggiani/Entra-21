def repetir(a: int, b: int):
    """ A função irá repetir o valor de (a) dado o número de (b) vezes"""

    lista = []
    for _ in range(b):
        lista.append(a)

    print(lista)

    return lista

numero_a = int(input("Digite um Número: "))
numero_b = int(input(f"Digite a quantidade de vezes que o numero {numero_a} irá repetir: "))
repetir(numero_a, numero_b)