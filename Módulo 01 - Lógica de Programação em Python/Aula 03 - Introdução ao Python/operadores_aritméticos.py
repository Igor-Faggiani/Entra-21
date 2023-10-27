"""
Operadores aritméticos são utilizados para realizar as operações do algoritmo.

Operadores Básicos:
- Adição: +
- Subtração: -
- Multiplicação: *
- Divisão: /
- Divisão Inteira: //
- Módulo: %
- Exponenciação: **

Precedência de Operadores:
1. Agrupamento ()
2. Exponenciação: **
3. Multiplicação, divisão e resto *, /, //, %
4. Adição e Subtração + e -

Operadores de Atribuição:
1. += -> x = 3 -> x += 5 -> x = 8
"""
import math

print(10 / 2 * 5)
print(math.sqrt(25))
print(math.floor(2.7))
print(math.ceil(2.1))

x = 5
x += 10
print(x)

print ('-x' * 50)