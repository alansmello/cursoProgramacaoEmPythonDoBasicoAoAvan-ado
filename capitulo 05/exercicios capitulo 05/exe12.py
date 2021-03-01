"""
Ler um número inteiro. Se o número lido for negativo, escreva a mensagem 'Número inválido'.
Se o número for positivo, calcular o logaritmo deste número.
"""
import math

num = int(input('digite um numero inteiro: '))

if num < 0:
    print('Número inválido.')
else:
    print(f'o Logaritmo de {num} é igual a {math.log10(num)}')
