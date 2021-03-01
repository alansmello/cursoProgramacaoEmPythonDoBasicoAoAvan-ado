"""
Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que:
A = ((base_maior + base_menor) * altura) / 2)
Lembre-se que a base maior e a base menor devem ser números maiores que zero.
"""

base_maior = float(input('digite o valor da base Maior do trapézio em centímetros:'))
base_menor = float(input('digite o valor da base Menor do trapézio em centímetros:'))
altura = float(input('digite o valor da Altura do trapézio em centímetros:'))
area = (((base_maior + base_menor) * altura) / 2)

if 0 < base_menor < base_maior:
    print(f'A área do trapézio é igual a {area:.2f} centímetros.')
else:
    print('Valores errados.')
