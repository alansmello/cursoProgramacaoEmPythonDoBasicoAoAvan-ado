"""
Leia a nota e o numero de faltas de um aluno e escreva o seu conceito. De acordo
com a tabela abaixo, quando o aluno tem mais de 20 faltas ocorre uma redução de
conceito.

NOTA              CONCEITO(ATÉ 20 FALTAS)     CONCEITO (MAIS DE 20 FALTAS)
9.0 até 10.00               A                               B
7.5 até 8.9                 B                               C
5.0 até 7.4                 C                               D
4.0 até 4.9                 D                               E
0.0 até 3.9                 E                               E
"""

nota = float(input('Digite a nota do aluno: '))
faltas = int(input('Digite o numero de faltas do aluno: '))

if 9.0 <= nota < 10.0:
    if faltas <= 20:
        print('Conceito: A')
    else:
        print('Conceito: B')
elif 7.5 <= nota < 9.0:
    if faltas <= 20:
        print('Conceito: B')
    else:
        print('Conceito: C')
elif 5.0 <= nota < 7.5:
    if faltas <= 20:
        print('Conceito: C')
    else:
        print('Conceito: D')
elif 4.0 <= nota < 5.0:
    if faltas <= 20:
        print('Conceito: D')
    else:
        print('Conceito: E')
elif 0 <= nota <4.0:
    print('Conceito: E')
