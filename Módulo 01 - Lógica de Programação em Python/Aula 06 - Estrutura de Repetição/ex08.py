print('''Cardápio:
x-Burger: R$10,00
x-Salada: R$12,00
x-Bacon: R$15,00
x-Tudo: R$18,00
''')

preco_xburger = 10
preco_xsalada = 12
preco_xbacon = 15
preco_xtudo = 18

pedido_xburger = int(input('Quantidade x-Burger: '))
pedido_xsalada = int(input('Quantidade x-Salada: '))
pedido_xbacon = int(input('Quantidade x-Bacon: '))
pedido_xtudo = int(input('Quantidade x-Tudo: '))

total_xburger = preco_xburger * pedido_xburger
total_xsalada = preco_xsalada * pedido_xsalada
total_xbacon = preco_xbacon * pedido_xbacon
total_xtudo = preco_xtudo * pedido_xtudo

total_pedido = total_xtudo + total_xbacon + total_xsalada + total_xburger

print(f'O total a pagar é de: R${total_pedido:.2f}')






