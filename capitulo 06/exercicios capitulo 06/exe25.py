"""
Faça um programa que some todos os números naturais abaixo de 1000 que são multiplos de 3 ou 5.
"""
number = 1000
soma = 0
print('Números naturais abaixo de 1000 que são multiplos de 3 ou 5:')
for i in range(0, number):
    if i % 3 == 0 or i % 5 == 0:
        print(f'{i} ', end='')
        soma+=i
print(f'\n\nSoma = {soma}')
