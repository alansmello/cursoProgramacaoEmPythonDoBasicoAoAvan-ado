"""
Uma empresa decide dar um aumento aos seus funcionários de acordo com uma tabela
que considera o salário atual e o tempo de serviço de cada funcionário. Os funcionários
com menor salário terão um aumento proporcionalmente maior do que os funcionários com
um salário maior, e conforme o tempo de serviço na empresa, cada funcionário irá
receber um bônus adicional de salário. faça um programa que leia:
- o valor do salário atual do funcionário;
- o tempo de serviço desse funcionário na empresa( número de anos de trabalho na empresa).

Use as tabela abaixo para calcular o salário reajustado deste funcionário e imprima o
valor do salário final reajustado, ou uma mensagem caso o funcionário não tenha direito
a nenhum aumento.

SALÁRIO ATUAL           REAJUSTE             TEMPO DE SERVIÇO          BÔNUS
Até 500,00              25%                  Abaixo de 1 ano           Sem Bônus
Até 1000,00             20%                  De 1 a 3 anos             100,00
Até 1500,00             15%                  De 4 a 6 anos             200,00
Até 2000,00             10%                  De 7 a 10 anos            300,00
Acima de 2000,00        Sem Reajuste         Mais de 10 anos           500,00
"""
salario_atual = float(input('Entre com o Salário Atual (R$): '))
tempo_servico = int(input('Entre com o tempo (anos) de serviços na empresa: '))

bonus = 0
salario_novo = 0

if 1 <= tempo_servico <= 3:
    bonus = 100
elif 4 <= tempo_servico <= 6:
    bonus = 200
elif 7 <= tempo_servico <= 10:
    bonus = 300
elif tempo_servico > 10:
    bonus = 500


if salario_atual <= 500:
    salario_novo = salario_atual + bonus + (salario_atual * 0.25)
    print(f'salário final reajustado: R${salario_novo:.2f}')
elif 500 < salario_atual <=1000:
    salario_novo = salario_atual + bonus + (salario_atual * 0.20)
    print(f'salário final reajustado: R${salario_novo:.2f}')
elif 1000 < salario_atual <= 1500:
    salario_novo = salario_atual + bonus + (salario_atual * 0.15)
    print(f'salário final reajustado: R${salario_novo:.2f}')
elif 1500 < salario_atual <= 2000:
    salario_novo = salario_atual + bonus + (salario_atual * 0.10)
    print(f'salário final reajustado: R${salario_novo:.2f}')
elif salario_atual > 2000:
    salario_novo = salario_atual + bonus
    print(f'salário final reajustado: R${salario_novo:.2f}')
