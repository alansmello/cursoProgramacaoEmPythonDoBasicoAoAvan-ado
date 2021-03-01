"""
Excreva um programa que, dada a idade de um nadador, classifique-o em uma das seguintes categorias:

CATEGORIA     IDADE
Infantil A    5 a 7
Infantil B    8 a 10
Juvenil A     11 a 13
Juvenil B     14 a 17
Sênior        maiores de 18
"""
idade = int(input('entre com a idade do nadador: '))

if 5 <= idade <= 7:
    print('Categoria: Infantil A.')
elif 8 <= idade <= 10:
    print('Categoria: Infantil B.')
elif 11 <= idade <= 13:
    print('Categoria: Juvenil A.')
elif 14 <= idade <= 17:
    print('Categoria: Juvenil B.')
elif idade >= 18:
    print('Categoria: Sênior.')
else:
    print('Muito Novo... Aguarde completar 5 anos.')
