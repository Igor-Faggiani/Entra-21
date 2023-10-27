lista1 = [1,3,4,5,10,11,12,15,17,19]
lista2 = [0,3,4,5,10,13,14,16,17,19]

elementos_comuns = [set(lista1) & set(lista2)]
print(elementos_comuns)