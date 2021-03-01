"""
Faça um programa que leia 10 inteiros e imprima sua média.
"""
soma = 0
for i in range(10):
    number = int(input(f'digite o valor {i+1}/10: '))
    soma += number
print(f'A media dos valores eh igual a {soma/10:.2f}')