"""
Faça um programa que receba a altura e o peso de uma pessoa. De acordo com a tabela
a seguir, verifique e mostre qual a classificação dessa pessoa:

ALTURA                               PESO
                    até 60      entre 60 e 90         Acima de 90
Menor que 1,20        A               D                    G
De 1,20 a 1,70        B               E                    H
Maior que 1,70        C               F                    I

"""
altura = float(input('Entre com sua altura (metros): '))
peso = float(input('Entre com seu peso (Kg): '))

if altura < 1.2:
    if peso <= 60:
        print('Classificação: A')
    elif 60 < peso <= 90:
        print('Classificação: D')
    else:
        print('Classificação: G')
elif 1.20 < altura <= 1.70:
    if peso <= 60:
        print('Classificação: B')
    elif 60 < peso <= 90:
        print('Classificação: E')
    else:
        print('Classificação: H')
else:
    if peso <= 60:
        print('Classificação: C')
    elif 60 < peso <= 90:
        print('Classificação: F')
    else:
        print('Classificação: I')
