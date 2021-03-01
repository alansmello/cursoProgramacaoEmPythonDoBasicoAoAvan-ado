"""
Faça um programa que leia um valor N inteiro e positivo, calcule e mostre o valor E,
conforme a fórmula a seguir:
E = 1+1/1! + 1/2! + 1/3! +...+1/n!
"""


def fatorial(num):
    n = num
    fat = 1
    i = 2
    while i <= n:
        fat = fat * i
        print(fat)
        i += 1

    return fat

print(0%2)



