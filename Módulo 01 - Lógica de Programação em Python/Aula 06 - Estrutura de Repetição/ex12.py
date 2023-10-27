# x = int(input('Digite um numero: '))
# y = int(input('Digite um numero: '))
# resultado = 1
#
# # 2^3 = 8 -> 2 x 2 x 2
# # 0 1 2
# for _ in range(y):
#     resultado *= x
#
# print(resultado)

x = int(input('Digite um numero: '))
y = int(input('Digite um numero: '))
resultado = 0

for _ in range(y):

    resultado += x

print(resultado)
