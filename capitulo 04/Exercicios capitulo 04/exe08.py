"""
Leia a temperatura em graus Kelvin e apresente-a em graus Celsius.
A fórmula de conversão é: C = K - 273.15, sendo C a temperatura em Celsius
e K a temperatura em Kelvin .
"""

kelvin = float(input('digite a temperatura em graus Kelvin: '))

celsius = kelvin - 273.15

print(f'a temperatura digitada, em Celsius é {celsius} graus')