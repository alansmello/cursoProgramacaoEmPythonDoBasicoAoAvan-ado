"""
Leia um valor de área em metros quadrados m² e apresente-o convertido em acres.
A fórmula de conversão é: A = M * 0.000247, sendo M a área em m² e A em acres.
"""

m2 = float(input('digite um valor de área em metro quadrado (m²): '))

acre = m2 * 0.000247

print(f'o valor convertido em "ACRES" é igual a {acre}.')
