"""
Faça um programa que peça ao usuário para digitar 10 valores e some-os.
"""
soma = 0
for i in range(10):
    number = int(input(f'digite o valor {i+1}/10: '))
    soma += number
print(f'o Tolal dos valores é igual a {soma}')
