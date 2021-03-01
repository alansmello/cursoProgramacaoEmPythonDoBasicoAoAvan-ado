"""
Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu
peso ideal, utilizando as seguintes fórmulas (onde h corresponde à altura):
* Homens: (72.7 * h) - 58
* Mulheres: (62.1*h) - 44.7
"""
sexo = int(input('digite (1) para homem (2) para mulher: '))
altura = float(input('digite sua altura em metros:'))

if sexo == 1:
    print(f'Seu peso ideal é {(72.7 * altura) - 58:.2f} kg.')
elif sexo == 2:
    print(f'Seu peso ideal é {(62.1 * altura) - 44.7:.2f} kg.')
else:
    print('opção inválida.')
