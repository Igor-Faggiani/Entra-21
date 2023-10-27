"""
20. Faça um programa que leia três números e exiba se eles formam um triângulo válido.
Um triângulo é válido se a soma de dois lados for maior que o terceiro lado.
"""

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

if numero1 + numero2 > numero3 and numero2 + numero3 > numero1 and numero1 + numero3 > numero2:
    print("O triângulo é válido")
else:
    print("O triângulo é inválido")
