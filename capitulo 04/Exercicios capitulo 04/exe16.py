"""
Leia um valor de comprimento em polegadas e apresente-o convertido em centimetros.
A fórmula de conversão é: C = P * 2.54, sendo C o comprimento em centimetros e P o comprimento em polegadas.
"""

polegada = float(input('digite um valor de comprimento em polegadas: '))

centimetro = polegada * 2.54

print(f'o valor convertido em centimetros é igual a {centimetro}.')
