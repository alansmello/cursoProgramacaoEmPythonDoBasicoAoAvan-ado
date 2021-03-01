"""
Faça um programa para verificar se um determinado número inteiro e divísel por
3 ou 5, mas não simultaneamente pelos dois.
"""
num = int(input('digite um número inteiro para verificar se é divísel por 3 ou 5, mas não simultaneamente pelos dois: '))

if (num % 3) == 0 and (num % 5) == 0:
    print('Não é o caso, pois é divisivel pelos dois.')
elif (num % 3) == 0 or (num % 5) == 0:
    print('Sim é o caso.')
else:
    print('Não é o caso, pois não é divisível por nenhum dos dois.')
