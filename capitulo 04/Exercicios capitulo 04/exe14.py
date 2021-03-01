"""
Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de conversão é: R = G * PI / 180,
sendo G o ângulo em graus e R em radianos e PI = 3.14.
"""

grau = float(input('digite um ângulo em grau: '))

pi = 3.14

radiano = grau * pi / 180

print(f'o valor informado convertido em radiano é igual a {radiano}')
