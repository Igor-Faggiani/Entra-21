valor_a = float(input('Digite um valor (A): '))
valor_b = float(input('Digite outro valor (B): '))
valor_c = float(input('Digite outro valor (C): '))

if valor_a > valor_b and valor_a > valor_c:
    print('O valor A é o maior!')
elif valor_a == valor_b < valor_c:
    print('O valor C é o maior!')
elif valor_c == valor_a < valor_b:
    print('O valor B é o maior!')
elif valor_b == valor_c < valor_a:
    print('O valor A é o maior!')
elif valor_a == valor_b > valor_c:
    print('Os Valores A e B são os maiores!')
elif valor_c == valor_a > valor_b:
    print('Os valores A e C são os maiores!')
elif valor_b == valor_c > valor_a:
    print('Os valores B e C são os maiores!')
elif valor_b > valor_c:
    print('O valor B é o maior!')
else:
    print('O valor C é o maior!')
