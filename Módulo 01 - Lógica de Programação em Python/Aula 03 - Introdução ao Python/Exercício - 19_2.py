nome = input('Digite seu nome: ')
salario = float(input('Digite seu salário: R$ '))
vendas = float(input('Digite o valor total de suas vendas: R$ '))
comissao = float(input('Digite o valor da comissão que você recebe por venda: %'))
calculo1 = vendas * comissao / 100
calculo2 = salario + calculo1
print(f'Somando o seu salário de R${salario}, mais as comissões de suas vendas, você receberá: R${calculo2:,.2f}')