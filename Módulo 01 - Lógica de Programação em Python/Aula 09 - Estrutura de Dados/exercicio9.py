"""
9. Construa um algoritmo que some todas os valores numéricos do dicionário abaixo e mostre o resultado na tela:

animais = {
"gatos": "Miaw",
"cachorros": 22,
"zebra": 10,
"girafa": 15,
"panda": 23,
"coala": 3
}
"""
animais = {
    "gatos": "Miaw",
    "cachorros": 22,
    "zebra": 10,
    "girafa": 15,
    "panda": 23,
    "coala": 3
}

soma = sum((valor for valor in animais.values() if isinstance(valor, int)))
print(soma)
