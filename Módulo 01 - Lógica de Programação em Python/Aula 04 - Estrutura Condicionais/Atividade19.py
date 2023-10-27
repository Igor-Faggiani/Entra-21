massa = float(input("Informe sua massa, em kg: "))
planeta = input("Informe o planeta no qual você quer saber o peso. Digite em caixa baixa: ")

match planeta:
    case "mercúrio":
        peso = massa*9.81*0.38
        print(f"Seu peso no planeta {planeta} é {peso:.2f} N ")
    case "vênus":
        peso = massa*9.81*0.91
        print(f"Seu peso no planeta {planeta} é {peso:.2f} N")
    case "marte":
        peso = massa*9.81*0.38
        print(f"Seu peso no planeta {planeta} é {peso:.2f} N ")
    case "júpiter":
        peso = massa*9.81*2.34
        print(f"Seu peso no planeta {planeta} é {peso:.2f} N")
    case "saturno":
        peso = massa*9.81*0.93
        print(f"Seu peso no planeta {planeta} é {peso:.2f} N")
    case "urano":
        peso = massa*9.81*0.92
        print(f"Seu peso no planeta {planeta} é {peso:.2f} N")
    case "netuno":
        peso = massa*9.81*1.12
        print(f"Seu peso no planeta {planeta} é {peso:.2f} N")
    case "plutão":
        peso = massa*9.81*0.06
        print(f"Seu peso no planeta {planeta} é {peso:.2f} N")
    case _:
        print("Você digitou incorretamente.")
