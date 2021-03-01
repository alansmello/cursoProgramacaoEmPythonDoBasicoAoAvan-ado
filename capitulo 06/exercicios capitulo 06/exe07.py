"""
Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua média.
"""
soma = 0
cont = 0
for i in range(10):
    number = int(input(f'digite o valor {i+1}/10: '))
    if number >= 0:
        soma += number
        cont += 1
print(f'A media dos valores positivos eh igual a {soma/cont:.2f}')
