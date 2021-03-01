"""
Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e
exiba na tela a média destas notas. Uma nota válida deve ser, obrigatoriamente, um
valor entre 0.0 e 10.0, onde caso a nota não possua um valor válido, este fato deve ser
informado ao usuário e o programa termina.
"""

nota01 = float(input('digite a primeira nota: '))
nota02 = float(input('digite a segunda nota: '))
media = (nota01 + nota02) / 2

if nota01 >= 0 and nota01 <= 10 and nota02 >= 0 and nota02 <= 10:
    print(f'média = {media} .')
else:
    print('notas inválidas')
