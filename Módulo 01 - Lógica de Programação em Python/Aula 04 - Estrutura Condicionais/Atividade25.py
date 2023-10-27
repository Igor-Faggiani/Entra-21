a = float(input("Informe o valor de a da equação de segundo grau: "))
if a == 0:
    print("A equação não é de segundo grau. ")
else:
    b = float(input("Informe o valor de b da equação de segundo grau: "))
    c = float(input("Informe o valor de c da equação de segundo grau: "))
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("A equação de segundo grau informada não possui raízes reais.")
    elif delta == 0:
        raiz = -1*b/2*a
        print(f"A equação de 2º grau informada possui apenas uma raiz, que é {raiz:.2f}, arredondadas")
    else:
        raiz1 = (- b + (delta ** (1/2)))/(2*a)
        raiz2 = (- b - (delta ** (1/2)))/(2*a)
        print(f"A equação informada possui 2 raízes reais, que são {raiz1:.2f} e {raiz2:.2f} ")
