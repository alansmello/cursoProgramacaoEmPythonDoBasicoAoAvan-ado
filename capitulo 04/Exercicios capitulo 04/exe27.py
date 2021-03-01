"""
Leia um valor de área em hectares e apresente-o convertido em metros quadrados m². A fórmula
de conversão é: M = H * 10000, sendo M a área em metros quadrados e H a área em hectares.
"""

hectares = float(input('digite um valor de área em hectares: '))

m2 = hectares * 10_000

print(f'o valor convertido em metros quadrados m² é igual a {m2:.2f} .')
