def somar(*args: int):
    """ A função irá retornar a soma dos numeros fornecidos"""

    resultado = 0
    for  numero in args:
        resultado += numero
    return print(resultado)


numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite um numero: "))
numero3 = int(input("Digite um numero: "))
numero4 = int(input("Digite um numero: "))
numero5 = int(input("Digite um numero: "))
somar(numero5, numero4, numero3, numero2, numero1)
