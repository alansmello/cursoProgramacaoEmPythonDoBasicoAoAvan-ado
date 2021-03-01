"""
Faça um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e a
segunda tem peso 1 e a terceira te peso 2. Ao final, mostrar a média do aluno e indicar
se o aluno foi aprovado ou reprovado. A nota para aprovação deve ser igual ou superior
a 6.0 pontos.
"""
nota1 = float(input('digite a nota 01: '))
nota2 = float(input('digite a nota 02: '))
nota3 = float(input('digite a nota 03: '))

media = (nota1 + nota2 + (nota3 * 2)) / 4

if media >= 6:
    print(f'APROVADO sua média ficou em {media:.2f} .')
else:
    print(f'REPROVADO sua média ficou em {media:.2f} .')
