"""
Faça um programa que leia um número inteiro N e depois imprima os N primeiros
numeros naturais ímpares.
"""
from random import sample
n = 5
numbers = sample(range(0, 100), 20)
cont = 0
print(f'numeros: {numbers}')
for i in numbers:
    if (i % 3) == 0:
        print(i)
        cont += 1
    if cont == n:
        break
