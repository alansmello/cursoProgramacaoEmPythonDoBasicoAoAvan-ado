"""
Leia um ângulo em radianos e apresente-o convertido em graus. A fórmula de conversão é: G = R * 180 / PI,
sendo G o ângulo em graus e R em radianos e PI = 3.14.
"""

radiano = float(input('digite um ângulo em radianos: '))

pi = 3.14

grau = radiano * 180 / pi

print(f'o valor informado convertido em graus é igual a {grau}')
