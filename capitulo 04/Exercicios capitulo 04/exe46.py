"""
Faça um programa que leia um numero inteiro positivo de três dígitos (de 100 a 999).
Gere outro número formado pelos dígitos invertidos do numero lido.
"""

cdu = int(input('Digite um número qualquer de 3 unidades: '))
centena = cdu//100
dezena = (cdu%100)//10
unidade = cdu%10
udc = unidade*100 + dezena*10 + centena
print('O valor invertido é ', udc)
