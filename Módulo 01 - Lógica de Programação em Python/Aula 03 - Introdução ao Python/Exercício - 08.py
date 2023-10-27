a = 10
b = 20
x = 2               # Variável auxiliar

a = a*x
b = b/x
print(a, b)

#Correção

a = 10
b = 20
a, b = b, a
print(a, b)
