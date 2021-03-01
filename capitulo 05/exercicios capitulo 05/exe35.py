"""
Leia uma data e determine se ela é válida. Ou seja, verifique se o mês está entre 1 e 12, e se o dia
existe naquele mês. Note que fevereiro tem 29 dias em anos bissextos, e 28 dias em anos não bissextos.
"""
dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))

if ano % 400 == 0 and mes == 2 and dia <= 29:
    print('Data Válida')
elif ano % 4 == 0 and ano % 100 != 0 and mes == 2 and dia <= 29:
    print('Data Válida')
elif mes == 2 and dia >= 29:
    print('Data Inválida')
elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia >= 31:
    print('Data Inválida')
elif (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12) and dia >= 32:
    print('Data Inválida')
else:
    print('Data Válida')
