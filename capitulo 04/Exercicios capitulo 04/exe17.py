"""
Leia um valor de comprimento em centimetros e apresente-o convertido em polegadas.
A fórmula de conversão é: P = C / 2.54, sendo C o comprimento em centimetros e P o comprimento em polegadas.
"""

centimetro = float(input('digite um valor de comprimento em centimetros: '))

polegada = centimetro / 2.54

print(f'o valor convertido em polegadas é igual a {polegada}.')
