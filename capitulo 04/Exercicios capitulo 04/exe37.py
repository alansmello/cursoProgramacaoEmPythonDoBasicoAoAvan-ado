"""
Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo em vista
que o desconto foi de 12%.
"""

produto = float(input('digite o valor do produto(R$): '))

desconto = produto * 0.12

print(f'O produto com 12% de desconto fica em : R${(produto - desconto):.2f}')
