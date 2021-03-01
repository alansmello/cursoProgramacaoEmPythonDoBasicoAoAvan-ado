"""
Em Matemática, o número harmônico designado por H(n) define-se como sendo a soma
da série harmónica:
H(n) = 1 + 1\2 + 1/3 + 1/4 + ... + 1/n
Faça um programa que leia um valor n inteiro e positivo e apresente o valor de H(n)
"""

number = int(input('digite um numero inteiro e positivo: '))

for i in range(1, 51):
    print(f'{number} / {i} = {number / i:.5f}')
