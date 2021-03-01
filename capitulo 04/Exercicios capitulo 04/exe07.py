"""
Leia a temperatura em graus Fahrenheit e apresente-a em graus Celsius.
A fórmula de conversão é: C = 5.0 * (F - 32.0) / 9.0, sendo C a temperatura em Celsius
e F a temperatura em Fahrenheit .

"""

fahrenheit = float(input('digite a temperatura em graus Fahrenheit: '))

celsius = 5.0 * (fahrenheit - 32.0) / 9.0

print(f'a temperatura digitada, em Celsius é {celsius} graus')