numero = float(input("Informe um número de 3 dígitos: "))
if numero > 0:
    digito1 = numero % 10
    digito2 = (numero // 10) % 10
    digito3 = numero // 100
    numero_invertido = digito1 * 100 + digito2 * 10 + digito3
    print(f"O número é positivo.")
    print(f"Seu inverso é {numero_invertido}")
else:
    print(f"O número não é positivo. Seu valor absoluto é {(-1)*numero} ")
