"""
Faça um programa que calcule e mostre a soma dos 50 primeiros numeros pares.
"""
from random import sample

numbers = sample(range(0, 1000), 200)
cont = 0
soma = 0
print(f'numeros: {numbers}')
for i in numbers:
    if (i % 2) == 0:
        print(i)
        soma += i
        cont += 1
    if cont == 50:
        break
print(f'Soma dos valores: {soma}')
