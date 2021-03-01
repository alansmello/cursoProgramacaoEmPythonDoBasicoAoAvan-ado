"""
Faça um programa que leia um numero e, caso ele seja positivo, calcule e mostre:
* O numero digitado ao quadrado;
* A raiz quadrada do numero digitado.
"""

import math

num = int(input('digite um numero: '))

if num > 0:
    print(f'a raiz de {num} é {math.sqrt(num):.2f} .')
    print(f'{num} ao quadrado é {(num**2):.2f}')
