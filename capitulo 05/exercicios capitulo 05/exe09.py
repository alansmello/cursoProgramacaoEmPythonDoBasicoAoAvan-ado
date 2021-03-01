"""
Leia o salario de um trabalhador e o valor da prestação de um emprestimo. Se a prestação
for maior que 20% do salário imprima:'Empréstimo não concedido', caso contrário imprima:
'Empréstimo concedido'.
"""
salario = float(input('digite o valor do seu salário(R$): '))
parcela_emprestimo = float(input('digite o valor da parcela do emprestimo(R$): '))

if parcela_emprestimo / salario > 0.20:
    print('Empréstimo não concedido')
else:
    print('Empréstimo concedido')
