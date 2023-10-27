medida1 = int(input("Digite a primeira medida: "))
medida2 = int(input("Digite a segunda medida: "))
medida3 = int(input("Digite a terceira medida: "))

if medida1 == medida2 == medida3:
    print("O triângulo é equilátero")
elif medida1 == medida2 or medida2 == medida3 or medida3 == medida1:
    print("O triângulo é isósceles")
else:
    print("O triângulo é escaleno")
