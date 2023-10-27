"""
15. Dado o dicionário de vendas abaixo, crie um algoritmo que retorne o total de faturamento da loja e o produto mais
vendido.

vendas = [
    {"produto": "camisa", "quantidade": 5, "preco_unitario": 20},
    {"produto": "calça", "quantidade": 2, "preco_unitario": 50},
    {"produto": "sapato", "quantidade": 3, "preco_unitario": 100}
]
"""
vendas = [
    {"produto": "camisa", "quantidade": 5, "preco_unitario": 20},
    {"produto": "calça", "quantidade": 2, "preco_unitario": 50},
    {"produto": "sapato", "quantidade": 3, "preco_unitario": 100}
]

total_faturamento = sum((produto["quantidade"] * produto["preco_unitario"] for produto in vendas))

maior_quantidade = 0
produto_mais_vendido = ""
for produto in vendas:
    if produto["quantidade"] > maior_quantidade:
        maior_quantidade = produto["quantidade"]
        produto_mais_vendido = produto["produto"]

print(f"""O total de faturamento é: R$ {total_faturamento:.2f}
O produto mais vendido foi {produto_mais_vendido} com {maior_quantidade} vendas realizadas.""")
