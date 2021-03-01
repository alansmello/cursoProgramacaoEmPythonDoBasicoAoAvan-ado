"""
Faça um programa que leia um número inteiro positivo N e calcule a soma dos n primeiros
números naturais
"""
from random import sample

num = 15
numbers = sample(range(0, 100), 30)
cont = 0
soma = 0
print(f'numeros: {numbers}')
for i in numbers:
    print(i)
    soma += i
    cont += 1
    if cont == num:
        break
print(f'Soma dos valores: {soma}')
