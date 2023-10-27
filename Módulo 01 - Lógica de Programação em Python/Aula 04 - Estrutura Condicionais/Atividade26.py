alimentacao = float(input("Informe seus gastos com alimentação, em R$: "))
moradia = float(input("Informe seus gastos com moradia, em R$: "))
transporte = float(input("Informe seus gastos com transporte, em R$: "))
lazer = float(input("Informe seus gastos com lazer, em R$: "))
saude = float(input("Informe seus gastos com saúde, em R$: "))
tv_internet_telefone = float(input("Informe seus gastos com tv, telefone e internet, em R$: "))
salario_mensal = float(input("Informe seu salário mensal, em R$: "))

despesas = alimentacao + moradia + transporte + lazer + saude + tv_internet_telefone
print(f"O percentual de gastos com alimentação em relação a seu salário é: {(alimentacao/salario_mensal)*100}%")
print(f"O percentual de gastos com moradia em relação a seu salário é: {(moradia/salario_mensal)*100}%")
print(f"O percentual de gastos com transporte em relação a seu salário é: {(transporte/salario_mensal)*100}%")
print(f"O percentual de gastos com lazer em relação a seu salário é: {(lazer/salario_mensal)*100}%")
print(f"O percentual de gastos com saude em relação a seu salário é: {(saude/salario_mensal)*100}%")
print(f"O percentual de gastos com tv, internet e "
      f"telefone em relação a seu salário é: {(tv_internet_telefone/salario_mensal)*100}%")
if despesas > salario_mensal:
    print("Suas despesas excedem seu salário mensal.")
elif despesas < salario_mensal:
    print("Seu salário é maior que suas despesas.")
else:
    print("Seu salário equivale a suas despesas.")
