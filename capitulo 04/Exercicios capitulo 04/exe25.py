"""
Leia um valor de área em acres e apresente-o convertido em metros quadrados m².
A fórmula de conversão é:  M = A * 4048.58, sendo M a área em m² e A em acres.
"""

acre = float(input('digite um valor de área em acres: '))

m2 = acre * 4048.58

print(f'o valor convertido em metros quadrados m² é igual a {m2}.')
