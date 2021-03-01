"""
Faça um algoritmo que encontre o primeiro múltiplo de 11, 13 ou 17 após um número dado.
"""
number = int(input('Digite um numero: '))
res = 0
for i in range(number+1, number+500):
    if i % 11 == 0 or i % 13 == 0 or i % 17 == 0:
        print(i)
        res = i
        break
if res % 11 == 0:
    print(f'O numero {res} é divisivel por 11. ')
if res % 13 == 0:
    print(f'O numero {res} é divisivel por 13. ')
if res % 17 == 0:
    print(f'O numero {res} é divisivel por 17. ')
