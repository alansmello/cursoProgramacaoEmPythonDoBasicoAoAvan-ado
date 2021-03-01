"""
Excreva um programa que, dados dois numeros inteiros, mostre na tela o maior deles,
assim como a diferença existente entre ambos.
"""

num1 =int(input('digite um numero: '))
num2 =int(input('digite outro numero: '))

if num1 > num2:
    print(f'O numero {num1} é maior.')
    print(f'a diferença entre os numeros digitados é {num1 - num2}')
else:
    print(f'O numero {num2} é maior.')
    print(f'a diferença entre os numeros digitados é {num2 - num1}')
