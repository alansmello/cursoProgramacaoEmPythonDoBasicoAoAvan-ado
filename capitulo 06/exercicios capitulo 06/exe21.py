"""
Faça um programa que receba 2 numeros. Calcule e mostre:
* a soma dos numeros pares desse intervalo de numeros, incluindo
os numeros digitados;
* a multiplicação dos numeros ímpares desse intervalo, incluindo os
digitados.
"""
n1 = 10
n2 = 25
soma = 0
mult = 1
for i in range(n1, n2+1, 2):
    print(i)
    soma += i
print(f'A soma dos valores é igual a {soma} .')

for i in range(n1+1, n2+1, 2):
    print(i)
    mult *= i
print(f'A multiplicação dos valores é igual a {mult} .')

