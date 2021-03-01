"""
Faça um programa que receba três números e mostre-os em ordem crescente.
"""

num = []
for i in range(3):
    num.append(int(input(f'Digite o {i+1}º numero:')))

num.sort()
print(f'seus números em ordem crescente {num}.')
