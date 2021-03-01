"""
Calcule as raízes da equação de 2º grau.
"""
import math


a = int(input('digite o nº "a" da equação de 2º grau: '))
b = int(input('digite o nº "b" da equação de 2º grau: '))
c = int(input('digite o nº "c" da equação de 2º grau: '))

delta = (b**2) - (4*a*c)

if delta < 0:
    print(f'Não existe raíz, pois o delta ({delta}) é negativo.')
else:
    x1 = (-b + (math.sqrt(delta))) / (2*a)
    x2 = (-b - (math.sqrt(delta))) / (2*a)
    if delta == 0:
        print(f'Raiz única igual x1 = {x1:.2f}, x2 = {x2:.2f}')
    else:
        print(f'As raizes são:  x1 = {x1:.2f} e x2 = {x2:.2f}')
