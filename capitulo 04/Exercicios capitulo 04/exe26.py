"""
Leia um valor de área em metros quadrados m² e apresente-o convertido em hectares. A fórmula
de conversão é: H = M * 0.0001, sendo M a área em metros quadrados e H a área em hectares.
"""

m2 = float(input('digite um valor de área em m²: '))

hectares = m2 * 0.0001

print(f'o valor convertido em hectares é igual a {hectares:} .')
