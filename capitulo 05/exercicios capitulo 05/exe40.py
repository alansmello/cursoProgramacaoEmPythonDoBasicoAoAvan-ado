"""
O custo ao consumidor de um carro novo é a soma do custo de fábrica, da comissão
do distribuidor, e dos impostos. A comissão e os impostos são calculados sobre o
custo de fábrica, de acordo com a tabela abaixo. Leia o custo de fábrica e escreva
o custo ao consumidor.

CUSTO DE FÁBRICA             % DO DISTRIBUIDOR          % DOS IMPOSTOS
Até R$12.000                         5                      isento
entre R$ 12000 e R$ 25.000          10                       15
acima de R$25.0000                  15                       20
"""

custo_fabrica = float(input('Entre com o valor (R$) dos custo de fábrica do automóvel: '))

if custo_fabrica <= 12.000:
    print(f'Valor ao consumidor: R${custo_fabrica + (custo_fabrica * 0.05):.2f}')
elif 12.000 < custo_fabrica <= 25.000:
    print(f'Valor ao consumidor: R${custo_fabrica + (custo_fabrica * 0.10) + (custo_fabrica * 0.15):.2f}')
else:
    print(f'Valor ao consumidor: R${custo_fabrica + (custo_fabrica * 0.15) + (custo_fabrica * 0.20):.2f}')
