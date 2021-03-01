"""
Escreva um programa que leia um número inteiro maior que zero e devolva, na tela, a soma
de todos os seus algarismos. Por exemplo, ao número 251 corresponderá o valor 8 (2+5+1).
Se o número lido não for maior do que zero, o programa terminará com a mensagem 'Número inválido'.
"""
num = int(input('digite um numero inteiro: '))
soma = 0

if num <=0 :
    print('Número inválido.')
else:
    while num >0:
        soma += num % 10
        num = num // 10
print(f'A soma dos algarismos é igual a {soma}.')
