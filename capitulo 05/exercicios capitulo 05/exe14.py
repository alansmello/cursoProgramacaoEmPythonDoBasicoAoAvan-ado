"""
A nota final de um estudante é calculada a partir de três notas atribuidas entre o intervalo
de 0 a 10, respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final.
A média das três notas mencionadas anteriormente obedece aos pesos:
* Trabalho de Laboratório: 2;
* Avaliação Semestral: 3;
* Exame Final: 5.
De acordo com o resultado, mostre na tela se o aluno está reprovado(média entre 0 e 2.9), de recuperação
(entre 3.0 e 4.9) ou se foi aprovado. Faça todas as verificações necessárias.
"""

trabalho_laboratorio = float(input('digite a nota do Trabalho de Laboratório: '))
avaliacao_semestral = float(input('digite a nota da Avaliação Semestral: '))
exame_final = float(input('digite a nota do Exame Final: '))

media = ((trabalho_laboratorio * 2) + (avaliacao_semestral * 3) + (exame_final * 5)) / 10

if media <= 2.9:
    print(f'REPROVADO - sua média ficou em {media} .')
elif media >2.9 and media <= 4.9:
    print(f'RECUPERAÇÃO - sua média ficou em {media} .')
else:
    print(f'APROVADO - sua média ficou em {media} .')

