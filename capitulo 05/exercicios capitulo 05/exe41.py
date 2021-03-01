"""
Faça um algoritmo que calcule o  IMC = peso/ (altura x altura) de uma pessoa e mostre sua classificação
de acordo com a tabela abaixo:
IMC              CLASSIFICAÇÃO
< 18.5           Abaixo do Peso
18.6 - 24.9      Saudável
25.0 - 29.9      Peso em excesso
30.0 - 34.9      Obesidade Grau I
35.0 - 39.9      Obesidade Grau II(severa)
>= 40.0          Obesidade Grau III(mórbida)
"""
peso = (float(input('Entre com o peso(Kg): ')))
altura = (float(input('Entre com a altura (metro): ')))

imc = peso / (altura * altura)

if imc <= 18.5:
    print(f'IMC: {imc:.2f} - Abaixo do peso')
elif 18.6 <= imc <25.00:
    print(f'IMC: {imc:.2f} - Saudável')
elif 25.00 <= imc < 30.00:
    print(f'IMC: {imc:.2f} - Peso em excesso')
elif 30.0 <= imc <35.00:
    print(f'IMC: {imc:.2f} - Obesidade Grau I')
elif 35.00 <= imc < 40.00:
    print(f'IMC: {imc:.2f} - Obesidade Grau II (severa)')
else:
    print(f'IMC: {imc:.2f} - Obesidade Grau III (mórmida)')
