"""
Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida em m/s (metros por segundo).
A fórmula de conversão é: M = K / 3.6, sendo K a velocidade em km/h e M em m/s.

"""

km = float(input('digite uma velocidade em Km/h: '))

metros_por_segundo = km / 3.6

print(f'a velocidade informada convertida em metros por segundo é igual a {metros_por_segundo:.2f} m/s.')
