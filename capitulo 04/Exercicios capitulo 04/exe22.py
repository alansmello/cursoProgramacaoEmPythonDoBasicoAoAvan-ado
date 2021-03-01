"""
Leia um valor de comprimento em jardas e apresente-o convertido em metros. A fórmula de conversão é:
M = 0.91 * J, sendo J o comprimento em jardas e M o comprimento em metros.
"""

jardas = float(input('digite um valor de comprimento em jardas: '))

metros = 0.91 * jardas

print(f'o valor convertido em metros é igual a {metros:.2f} .')
