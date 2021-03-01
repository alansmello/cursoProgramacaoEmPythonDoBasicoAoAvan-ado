"""
Escreva um programa que leia um numero inteiro e calcule a soma de todos os divisores
desse numero, com exceção dele próprio. Ex: a soma dos divisores do numero 66 é
1+2+3+6+11+22+33 = 78
"""
number = 336
soma = 0
print(f'divisores de {number}:')

for i in range(1, number+1):
    if (number % i) == 0:
        print(f'{i} ', end='')
        soma += i

print(f'\n\nA soma dos divisores de {number}, com exceção dele próprio, é igual a {soma - number}.')
