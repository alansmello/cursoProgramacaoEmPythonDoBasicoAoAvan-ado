"""
Leia um valor de massa em quilogramas e apresente-o convertido em libras. A fórmula de conversão é:
L = K / 0.45, sendo K a massa em quilogramas e L a massa em libras.
"""

quilograma = float(input('digite um valor de massa em quilogramas: '))

libra = quilograma / 0.45

print(f'o valor convertido em libras é igual a {libra:.2f}')
