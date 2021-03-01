"""
Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo
que ele recebeu um aumento de 25%.
"""

salario_antigo = float(input('digite seu salário(R$): '))

salario_novo = salario_antigo + (salario_antigo * 0.25)

print(f'Seu salário com aumento de 25% fica em R${salario_novo:.2f}')
