"""
Escreva um algoritmo que leia um número inteiro entre 100 e 999 e imprima
na saída cada um dos algarismos que compõem o numero.
"""
number = 100
centena = number//100
dezena = number - (centena * 100)
dezena = dezena//10
unidade = number - (centena * 100) - (dezena * 10)

print(f'{centena} - {dezena} - {unidade}')

