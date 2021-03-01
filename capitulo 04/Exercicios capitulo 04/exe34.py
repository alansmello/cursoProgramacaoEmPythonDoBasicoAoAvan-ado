"""
Leia o valor do raio de um circulo e calcule e imprima a área do circulo correspondente.
A área do circulo é PI * raio², considere PI = 3.141592.
"""

pi = 3.141592

raio = float(input('digite o valor do raio de um circulo: '))

area = pi * (raio**2)

print(f'a area do circulo é igual a {area:.2f} .')
