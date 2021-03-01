"""
Leia uma distância em quilômetros e apresente-a convertida em milhas. A fórmula de conversão é: M = K /  1.61,
sendo K a distância em quilômetros e M em milhas.
"""

quilometros = float(input('digite uma distância em quilômetros: '))

milhas = quilometros / 1.61

print(f'a distância digitada convertida em milhas é igual a {milhas:.2f} milhas.')
