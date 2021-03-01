"""
Faça um algoritmo que leia um numero positivo e imprima seus divisores.
"""
number = 1250

for i in range(1, number+1):
    if (number % i) == 0:
        print(f' O numero {i} é divisor de {number}')