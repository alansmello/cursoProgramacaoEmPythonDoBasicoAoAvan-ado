"""
Escreva um programa que leia as coordenadas x e y de pontos no R² e calcule sua distância de origem(0,0).
"""
import math

x = int(input('digite o valor de x: '))
y = int(input('digite o valor de y: '))

resultado = math.sqrt(x**2 + y**2)

print(f'o resultado é {resultado:.2f} .')
