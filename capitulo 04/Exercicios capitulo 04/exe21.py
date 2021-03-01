"""
Leia um valor de massa em libras e apresente-o convertido em quilogramas . A fórmula de conversão é:
K = L * 0.45, sendo K a massa em quilogramas e L a massa em libras.
"""

libra = float(input('digite um valor de massa em libras: '))

quilograma = libra * 0.45

print(f'o valor convertido em quilogramas é igual a {quilograma:.2f}')
