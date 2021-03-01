"""
Leia um valor de volume em litros e apresente-o convertido em metros cúbicos m3 . A fórmula de conversão é:
M = L / 1000, sendo L o volume em litros e M o volume em metros cúbicos.
"""

litro = float(input('digite um valor em litros: '))

metro_cubico = litro / 1000

print(f'o valor convertido em metro_cubico é igual a {metro_cubico:.2f}')
