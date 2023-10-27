ano = int(input("Informe um ano: "))
if ano % 4 == 0:
    if ano % 100 != 0:
        if ano % 400 == 0:
            print("O ano é bissexto.")
    print("O Ano é bissexto.")
else:
    print("O ano não é bissexto. ")
