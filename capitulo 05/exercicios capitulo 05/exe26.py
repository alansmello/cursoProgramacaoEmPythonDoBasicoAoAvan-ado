"""
Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro
em um percurso, calcule o consumo em Km/l e escreva uma mensagem de acordo com
a tabela abaixo:

COMSUMO       KM/L     MENSAGEM
menor que     8        Venda o carro!
entre         8 e 14   Econômico!
maior que     14       Super econômico!
"""
km = float(input('entre com a distância percorrida (Km): '))
litros = float(input('entre com a quantidade de litros consumidos: '))

consumo = km/litros

if consumo < 8:
    print(f'Venda o carro! Consumo igual a {consumo:.2f}Km/l.')
elif 8 < consumo <= 14:
    print(f'Econômico! Consumo igual a {consumo:.2f}Km/l.')
else:
    print(f'Super Econômico! Consumo igual a {consumo:.2f}Km/l.')
