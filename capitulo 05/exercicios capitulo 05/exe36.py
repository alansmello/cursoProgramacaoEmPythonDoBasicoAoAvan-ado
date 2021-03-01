"""
Escreva um programa que, dado o valor da venda, imprima a comissão que deverá ser paga
ao vendedor. Para calcular a comissão, considere a tabela abaixo:

VENDA MENSAL                                                     COMISSÃO
Maior ou igual a R$100.000,00                                    R$700,00 + 16% das vendas
Menor que R$100.000,00 e maior ou igual a R$80.000,00            R$650,00 + 14% das vendas
Menor que R$80.000,00 e maior ou igual a R$60.000,00             R$600,00 + 14% das vendas
Menor que R$60.000,00 e maior ou igual a R$40.000,00             R$550,00 + 14% das vendas
Menor que R$40.000,00 e maior ou igual a R$20.000,00             R$500,00 + 14% das vendas
Menor que R$20.000,00                                            R$400,00 + 14% das vendas
"""

venda = float(input('Digite o valor da venda(R$): '))

if venda >= 100.000:
    print(f'Valor da comissão: R${700 + (venda * 0.16):.2f}')
elif 80.000 <= venda < 100.000:
    print(f'Valor da comissão: R${650 + (venda * 0.14):.2f}')
elif 60.000 <= venda < 80.000:
    print(f'Valor da comissão: R${600 + (venda * 0.14):.2f}')
elif 40.000 <= venda < 60.000:
    print(f'Valor da comissão: R${550 + (venda * 0.14):.2f}')
elif 20.000 <= venda < 40.000:
    print(f'Valor da comissão: R${500 + (venda * 0.14):.2f}')
else:
    print(f'Valor da comissão: R${400 + (venda * 0.14):.2f}')
