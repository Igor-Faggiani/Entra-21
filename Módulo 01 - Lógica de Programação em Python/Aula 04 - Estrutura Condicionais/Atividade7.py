salario = float(input('Digite seu salário: '))
emprestimo = float(input('Digite o valor da prestação do empréstimo: '))

if emprestimo / salario > 0.2:
    print('O empréstimo não é concedido! ')
else:
    print('Empréstimo concedido!')
