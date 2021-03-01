"""
Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro. O volume de um
cilindro circular é calculado por meio da seguinte fórmula: V = PI * raio² * altura, onde PI - 3.141592.
"""
pi = 3.141592
altura = float(input('digite a altura: '))
raio = float(input('digite o raio: '))

volume = pi * (raio**2) * altura

print(f'o volume do cilindro é igual a {volume:.2f} .')
