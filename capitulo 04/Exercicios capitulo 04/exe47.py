"""
Leia um numero inteiro de 4 dígitos (de 1000 a 9999) e imprima 1 dígito por linha.
"""

num = int(input('digite uma milhar: '))

milhar = num//1000
centena = (num%1000)//100
dezena = (num%100)//10
unidade = num%10

print(f'{milhar}')
print(f'{centena}')
print(f'{dezena}')
print(f'{unidade}')