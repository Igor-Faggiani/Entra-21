numero1 = float(input("Informe um número: "))
operador = input("Informe o operador: (+) Adição, (-) Subtração, (*) Multiplicação, (/) Divisão ")
numero2 = float(input("Informe outro número: "))


if operador == "+":
    resultado = numero1 + numero2
    print(f"O resultado da soma é: {resultado:.2f}")
elif operador == "-":
    resultado = numero1 - numero2
    print(f"O resultado da subtração é: {resultado:.2f}")
elif operador == "*":
    resultado = numero1 * numero2
    print(f"O resultado da multiplicação é: {resultado:.2f}")
elif operador == "/":
    resultado = numero1 / numero2
    print(f"O resultado da divisão é: {resultado:.2f}")
else:
    print("Operador incorreto, execute o programa novamente. ")
