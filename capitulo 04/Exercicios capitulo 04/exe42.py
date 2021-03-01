"""
Receba o salário-base de um funcionário. Calcule e imprima o salário a receber,
sabendo-se que esse funcionário tem uma gratificação de 5% sobre o salário-base. Além disso,
ele paga 7% de imposto sobre o salário-base.
"""

salario_base = 2700
gratificacao = 2700 * 0.05
imposto = 2700 * 0.07

print(f'total a receber -> R${((salario_base + gratificacao) - imposto):.2f} .')
