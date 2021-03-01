"""
Faça um programa que mostre ao usuário um menu com 4 opções de operações matemáticas
(as básicas, por exemplo). O usuário escolhe uma das opções e o seu programa então pede
dois valores numéricos e realiza a operação, mostrando o resultado e saindo.
"""
import os

print('ESCOLHA UMA DAS OPÇÕES A SEGUIR:')
print('[1] SOMA')
print('[2] SUBTRAÇÃO')
print('[3] MULTIPLICAÇÃO')
print('[4] DIVISÃO')
operacao = int(input('\n\n\nDigite sua escolha: '))



num1 = int(input('digite um valor:'))
num2 = int(input('digite outro valor:'))



if operacao == 1:
    print(f'O resultado é {num1 + num2} .')
if operacao == 2:
    print(f'O resultado é {num1 - num2} .')
if operacao == 3:
    print(f'O resultado é {num1 * num2} .')
if operacao == 4:
    print(f'O resultado é {num1 / num2} .')
else:
    print('Escolha de operação inválida')
