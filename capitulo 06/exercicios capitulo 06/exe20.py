"""
Ler uma sequencia de números inteiros e determinar se eles são pares ou não.
Deverá ser informado o numero de dados lidos e numero de valores pares. O
processo termina quando for digitado o numero 100.
"""
from random import sample

finish = 0

while finish != 100:
    cont = 0
    num = sample(range(10, 20), 1)
    numbers = sample(range(0, 200), num[0])
    print(f'numeros: {numbers}')
    for i in numbers:
        if (i % 2) == 0:
            cont += 1
    print(f'Foram lidos {len(numbers)} e tiveram {cont} numeros pares.')
    finish = (int(input('Para terminar o processo digite 100, ou qualquer outro valor para continuar: ')))
