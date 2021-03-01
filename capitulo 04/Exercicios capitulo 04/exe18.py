"""
Leia um valor de volume em metros cúbicos m3 e apresente-o convertido em litros. A fórmula de conversão é:
L = M * 1000, sendo L o volume em litros e M o volume em metros cúbicos.
"""

metro_cubico = float(input('digite um valor em metros cúbicos: '))

litro = 1000 * metro_cubico

print(f'o valor convertido em litros é igual a {litro:.2f}')
