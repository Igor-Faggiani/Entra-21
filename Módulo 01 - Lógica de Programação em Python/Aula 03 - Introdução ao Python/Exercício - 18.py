preco = float(input('Digite o preço do seu produto: '))
desconto = float(input('Digite o desconto do produto: '))
x = preco * desconto / 100
valor_final = preco - x
print(f'O produto com o preço de R${preco:.2f} terá o desconto de R${x:.2f}, sendo o valor final de R${valor_final:.2f}.')