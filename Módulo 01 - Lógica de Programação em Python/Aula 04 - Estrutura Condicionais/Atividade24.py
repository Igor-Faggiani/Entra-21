numero1 = float(input("Informe um número: "))
numero2 = float(input("Informe outro número: "))
numero3 = float(input("Informe mais um número: "))
if numero1 > numero2 and numero1 > numero3:
    if numero2 > numero3:
        print(f"A ordem decrescente dos números é: {numero1},{numero2},{numero3}")
    else:
        print(f"A ordem decrescente dos números é: {numero1},{numero3},{numero2}")
elif numero2 > numero1 and numero2 > numero3:
    if numero1 > numero3:
        print(f"A ordem decrescente dos números é: {numero2},{numero1},{numero3}")
    else:
        print(f"A ordem decrescente dos números é: {numero2},{numero3},{numero1}")
elif numero3 > numero1 and numero3 > numero2:
    if numero1 > numero2:
        print(f"A ordem decrescente dos números é: {numero3},{numero1},{numero2}")
    else:
        print(f"A ordem decrescente dos números é: {numero3},{numero2},{numero1}")
else:
    print("Valor inválido.")
