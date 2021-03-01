"""
Determine se um determinado ano lido é bissexto. Sendo que um ano é bissexto se
for divisível por 400 ou se for divisível por 4 e não for divisível por 100. Por
exemplo: 1988, 1992, 1996.
"""
ano = int(input('Digite um ano: '))

if ano % 400 == 0:
    if ano == 2021:
        print(f'Sim, o ano {ano} é Bissexto.')
    elif ano > 2021:
        print(f'Sim, o ano {ano} vai ser Bissexto.')
    else:
        print(f'Sim, o ano {ano} foi Bissexto.')
elif ano % 4 == 0 and ano % 100 != 0:
    if ano == 2021:
        print(f'Sim, o ano {ano} é Bissexto.')
    elif ano > 2021:
        print(f'Sim, o ano {ano} vai ser Bissexto.')
    else:
        print(f'Sim, o ano {ano} foi Bissexto.')
else:
    if ano == 2021:
        print(f'Não, o ano {ano} não é Bissexto.')
    elif ano > 2021:
        print(f'Não, o ano {ano} não vai ser Bissexto.')
    else:
        print(f'Não, o ano {ano} não foi Bissexto.')
