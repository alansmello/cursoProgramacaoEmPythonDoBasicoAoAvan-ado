"""
Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado
possui uma taxa diferente de imposto sobre o produto(MG 7%; SP 12%; RJ 15%;
MS 8%). Faça um programa em que o usuário entre com o valor e o estado destino do
produto e o programa retorne o preço final do produto acrescido do imposto do
estado em que será vendido. Se o estado digitado não for válido, mostrar uma mensagem
de erro.
"""

valor = float(input('Digite o valor do produto:'))

estado = int(input("""\nDigite qual Estado será o destino da venda:

Minas Gerais       [1]
São Paulo          [2]
Rio de Janeiro     [3]
Mato grosso do Sul [4]

entre com o código: """))

if estado == 1:
    print(f'o valor final do produto é igual a R${valor + (valor * 0.07):.2f}')
elif estado == 2:
    print(f'o valor final do produto é igual a R${valor + (valor * 0.12):.2f}')
elif estado == 3:
    print(f'o valor final do produto é igual a R${valor + (valor * 0.15):.2f}')
elif estado == 4:
    print(f'o valor final do produto é igual a R${valor + (valor * 0.08):.2f}')
else:
    print('Código invalido.')
