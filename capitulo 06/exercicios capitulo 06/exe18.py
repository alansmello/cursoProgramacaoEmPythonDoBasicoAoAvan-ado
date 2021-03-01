"""
Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles e
quantas vezes o maior numero foi lido. A quantidade de números a serem lidos deve
ser fornecida pelo usuário.
"""
qtd = int(input('Digite a quantidade de numeros a ser lido: '))
numbers = []

for i in range(1, qtd+1):
    numbers.append(int(input(f'Digite o numero {i}/{qtd}: ')))

print(f'O maior numero digitado foi o {max(numbers)}, ele foi digitado {numbers.count(max(numbers))} vezes.')
