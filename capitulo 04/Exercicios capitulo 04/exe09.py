"""
Leia a temperatura em graus Celsius e apresente-a em graus Kelvin.
A fórmula de conversão é: K = C + 273.15, sendo K a temperatura em Kelvin
e K a temperatura em Celsius .
"""

celsius = float(input('digite a temperatura em graus Celsius: '))

kelvin = celsius + 273.15

print(f'a temperatura digitada, em Kelvin é {kelvin:.2f} graus')