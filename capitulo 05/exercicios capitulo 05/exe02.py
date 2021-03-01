"""
Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do numero.
Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.
"""
import math

num = int(input('digite um numero: '))

if num > 0:
    print(f'a raiz de {num} é {math.sqrt(num):.2f} .')
else:
    print('O número é inválido.')
