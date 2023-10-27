montante_inicial = float(input('Digite o montante inicial: R$'))
taxa_juros = float(input('Digite a taxa de juros: %'))
periodo = float(input('Digite o período de tempo: '))
taxa_decimal = taxa_juros / 100
calculo = montante_inicial * (taxa_decimal + 1) ** periodo
print(f'Ao final de {periodo:.0f} meses, ao juros de {taxa_juros}%, você terá acumulado um total de: {calculo:.2f}R$')
