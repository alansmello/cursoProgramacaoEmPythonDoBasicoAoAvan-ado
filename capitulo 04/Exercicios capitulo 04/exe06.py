"""
Leia a temperatura em graus Celsius e apresente-a em graus Fahrenheit.
A fórmula de conversão é: F=C*(9.0/9.5)+32.0, sendo F a temperatura em Fahrenheit
e C a temperatura em Celsius.

"""

celsius = float(input('digite a temperatura em graus Celsius: '))

fahrenheit = celsius * (9.0/9.5) + 32.0

print(f'a temperatura digitada, em Fahrenheit é {fahrenheit} graus')

