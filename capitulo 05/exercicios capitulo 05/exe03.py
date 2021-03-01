"""
Leia um número real. Se o número for positivo imprima a raiz quadrada. Do contrário,
imprima o número ao quadrado.
"""
import math

num = float(input('digite um numero: '))

if num > 0:
    print(f'a raiz de {num} é {math.sqrt(num):.2f} .')
else:
    print(f'{num} ao quadrado é {(num**2):.2f}')
