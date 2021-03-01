"""
Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em km/h (quilômetros por hora) .
A fórmula de conversão é: K = M * 3.6, sendo  M a velocidade em m/s e K  em km/h.

"""

metros_por_segundo = float(input('digite uma velocidade em metros por segundo: '))

km = metros_por_segundo * 3.6

print(f'a velocidade informada convertida em quilômetros por hora é igual a {km:.2f} km/h.')