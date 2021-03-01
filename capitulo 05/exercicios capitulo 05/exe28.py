"""
Faça um programa que leia três numeros inteiros positivos e efetue o cãlculo de uma das
seguintes médias de acordo com um valor numérico digitado pelo usuário:
(a) Geométrica:
(b) Ponderada:
(c) Harmônica:
(d) Aritmética:
"""
import math

x = int(input('digite um numero inteiro (x): '))
y = int(input('digite um numero inteiro (y): '))
z = int(input('digite um numero inteiro (z): '))

print('Escolha um calculo de Media:')
print("""(a) Geométrica:
(b) Ponderada:
(c) Harmônica:
(d) Aritmética:""")
escolha = str(input('\nDigite sua escolha: ')).upper()

if escolha == 'A':
    print(f'Media Geométrica = {math.pow(x*y*z,1/3):.2f}')
elif escolha == 'B':
    print(f'Media Ponderada = {(x+2*y+3*z)/6:.2f}')
elif escolha == 'C':
    print(f'Media Harmônica = {1/(1/x + 1/y + 1/z):.2f}')
elif escolha == 'D':
    print(f'Media Aritmética = {(x+y+z)/3:.2f}')
else:
    print('Escolha inválida!')
