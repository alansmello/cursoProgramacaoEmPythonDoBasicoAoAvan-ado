"""
Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço antigo,
calcule e escreva o preço novo, e escreva uma mensagem em função do preço novo
(de acordo com a segunda tabela).

PREÇO ANTIGO         PERCENTUAL DE AUMENTO
até R$50                       5%
entre R$50 e R$100             10%
acima de R$100                 15%


PREÇO NOVO                              MENSAGEM
até R$80                                 Barato
entre R$80 e R$120(inclusive)            Normal
entre R$120 e R$200(inclusive)           Caro
acima de R$200                           Muito Caro
"""

preco_antigo = float(input('Digite o preço antigo: '))


if preco_antigo <= 50.00:
    preco_novo = preco_antigo + (preco_antigo * 0.05)
    print(f'Preço Novo R${preco_novo:.2f}. Barato.')
elif 50.00 < preco_antigo <= 100.00:
    preco_novo = preco_antigo + (preco_antigo * 0.1)
    if preco_novo <= 80.00:
        print(f'Preço Novo R${preco_novo:.2f}. Barato.')
    else:
        print(f'Preço Novo R${preco_novo:.2f}. Normal.')
elif preco_antigo > 100.00:
    preco_novo = preco_antigo + (preco_antigo * 0.15)
    if 80 < preco_novo <= 120:
        print(f'Preço Novo R${preco_novo:.2f}. Normal.')
    elif 120 < preco_novo <= 200:
        print(f'Preço Novo R${preco_novo:.2f}. Caro.')
    else:
        print(f'Preço Novo R${preco_novo:.2f}. Muito Caro.')
