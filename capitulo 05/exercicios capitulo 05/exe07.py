"""
Faça um programa que receba dois numeros e mostre o maior. Se por acaso, os dois
numeros forem iguais, imprima a mensagem 'Numeros iguais'.
"""
num1 =int(input('digite um numero: '))
num2 =int(input('digite outro numero: '))

if num1 > num2:
    print(f'O numero {num1} é maior.')
elif num1 == num2:
    print(f'Numeros iguais.')
else:
    print(f'O numero {num2} é maior.')
