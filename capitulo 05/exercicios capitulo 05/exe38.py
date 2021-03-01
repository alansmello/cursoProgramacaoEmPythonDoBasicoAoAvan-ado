"""
Leia uma data de nascimento de uma pessoa pornecida atravé de três numeros inteiros:
Dia, Mês e Ano. Tesete a validade desta data para saber se esta é uma data válida. Teste
se o dia fornecido é um dia válido: dia > 0, dia <=28 para o mês de fevereiro (29 se o ano
for bissexto), dia <= 30 em abril, junho, setembro e novembro, dia <= 31 nos outros meses.
Teste a validade do mês: mês >0 e mês <13. Teste a validade do ano: ano <= ano atual(use
uma constante definida com o valor igual ao ano atual). Imprimir: "data válida" ou "data
inválida" no final da execução do programa.
"""
ano_atual = 2021

dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))

if ano % 400 == 0 and mes == 2 and 0 < dia <= 29:
    if ano <= ano_atual:
        print('Data Válida')
    else:
        print('Data Inválida')
elif ano % 4 == 0 and ano % 100 != 0 and mes == 2 and 0 < dia <= 29:
    if ano <= ano_atual:
        print('Data Válida')
    else:
        print('Data Inválida')
elif mes == 2 and dia >= 29:
    if ano <= ano_atual:
        print('Data Inválida')
    else:
        print('Data Inválida')
elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and 0 < dia >= 31:
    if ano <= ano_atual:
        print('Data Inválida')
    else:
        print('Data Inválida')
elif (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12) and 0 < dia >= 32:
    if ano <= ano_atual:
        print('Data Inválida')
    else:
        print('Data Inválida')
else:
    if ano <= ano_atual:
        print('Data Válida')
    else:
        print('Data Inválida')
