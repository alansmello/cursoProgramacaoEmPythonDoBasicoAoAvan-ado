"""
Leia uma distância em milhas e apresente-a convertida em quilômetros. A fórmula de conversão é: K = 1.61 * M,
sendo K a distância em quilômetros e M em milhas.
"""

milhas = float(input('digite uma distância em milhas: '))

quilometros = 1.61 * milhas

print(f'a distância digitada convertida em quilômetros é igual a {quilometros:.2f} quilômetros.')
