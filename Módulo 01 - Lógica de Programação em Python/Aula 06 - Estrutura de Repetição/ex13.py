dividendo = int(input('Digite um numero: '))
divisor = int(input('Digite um numero: '))
resultado = 0

while dividendo >= divisor:
    dividendo -= divisor
    resultado += 1

print(resultado)