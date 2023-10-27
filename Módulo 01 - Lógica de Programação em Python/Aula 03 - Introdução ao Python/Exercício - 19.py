nome = input('Nome do vendedor: ')
salario = 2000
vendas = 1150.50
calculo1 = vendas * 15 / 100
calculo2 = calculo1 + salario
print(f'Somando o seu salário de R${salario} mais as comissões de 15% sobre suas vendas, você receberá: R${calculo2:.2f}')
