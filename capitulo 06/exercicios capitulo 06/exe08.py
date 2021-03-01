"""
Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.
"""
number = []

for i in range(10):
    number.append(int(input(f'digite o valor {i+1}/10: ')))

print(f'Maior numero: {max(number)}')
print(f'Menor numero: {min(number)}')
