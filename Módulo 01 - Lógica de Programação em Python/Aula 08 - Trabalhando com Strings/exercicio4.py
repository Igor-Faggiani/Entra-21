nomes = input('Digite um nome: ').split()

if len(nomes) < 3:
    nome_abreviado = ''
    for nome in nomes:
        #.upper Transforma em maiúsculo
        nome_abreviado += nome[0].upper()
    print(nome_abreviado)
else:
    nome_abreviado = [nome[0].upper() + "." for nome in nomes[1:-1]]
    # for nome in nomes[1:-1]:
    #     nome_abreviado.append(nome[0].upper() + '.')
    print(f'{nomes[0]} {" ".join(nome_abreviado)} {nomes[-1]}')