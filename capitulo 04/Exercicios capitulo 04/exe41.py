"""
Faça um programa que leia o valor da hora de trabalha (em reais) e número de horas trabalhadas no mês.
Imprima o valor a ser pago ao funcionário, adicionando 10% sobre o valor calculado.
"""

valor_hora_trabalhada = float(input('digite o valor da hora trabalhada(R$): '))

quant_horas = float(input('digite a quantidade de horas trabalhadas: '))

total = (valor_hora_trabalhada * quant_horas)

adicional = total * 0.10

print(f'O total a receber é R$ {(total + adicional):.2f} .')
