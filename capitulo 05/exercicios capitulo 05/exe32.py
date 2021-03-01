"""
Escrever um programa que leia o código escolhido do cardápio de uma lanchonete e a quantidade.
O programa deve calcular o valor a ser pago por aquele lanche. Considere que a cada execução
somente será calculado um pedido. O cardápio da lanchonete segue o padrão abaixo:

ESPECIFICAÇÃO      CÓDIGO     PREÇO
cachorro quente    100        1,20
bauru simples      101        1,30
bauru com ovo      102        1,50
hamburguer         103        1,20
chesburguer        104        1,70
suco               105        2,20
refrigerante       106        1,00
"""
import os


print("==============CARDÁPIO=============")
print("""ESPECIFICAÇÃO      CÓDIGO     PREÇO
cachorro quente    100        1,20
bauru simples      101        1,30
bauru com ovo      102        1,50
hamburguer         103        1,20
chesburguer        104        1,70
suco               105        2,20
refrigerante       106        1,00""")

pedido = 1
while pedido == 1:

    escolha = int(input('\ndigite o código: '))

    quantidade = int(input('digite a quantidade: '))

    if escolha == 100:
        print(f'Total do pedido = R${quantidade * 1.20:.2f}')
    elif escolha == 101:
        print(f'Total do pedido = R${quantidade * 1.30:.2f}')
    elif escolha == 102:
        print(f'Total do pedido = R${quantidade * 1.50:.2f}')
    elif escolha == 103:
        print(f'Total do pedido = R${quantidade * 1.20:.2f}')
    elif escolha == 104:
        print(f'Total do pedido = R${quantidade * 1.70:.2f}')
    elif escolha == 105:
        print(f'Total do pedido = R${quantidade * 2.20:.2f}')
    elif escolha == 106:
        print(f'Total do pedido = R${quantidade * 1.00:.2f}')

    pedido = int(input('\nOutro pedido? (1)SIM (2)NÃO: '))
