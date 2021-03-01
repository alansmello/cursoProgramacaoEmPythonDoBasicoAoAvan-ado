"""
Uma empresa contrata um encanador a R$30,00 por dia. Faça um programa que solicite o numero de dias trabalhados pelo
encanador e imprima a quantia líquida que deverá ser paga, sabendo-se que são descontados 8% para impostos de renda.

"""

dias_trabalhados = float(input('digite a quantidade de dias trabalhados: '))

total = dias_trabalhados * 30
imposto_renda = total * 0.08
total_liquido = total - imposto_renda

print(f'o total líquido a receber é R${total_liquido:.2f} .')
