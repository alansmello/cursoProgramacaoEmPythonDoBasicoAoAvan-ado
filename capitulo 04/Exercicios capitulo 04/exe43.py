"""
Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:

-> o total a pagar com desconto de 10%;
-> o valor de cada parcela, no parcelamento de 3x sem juros;
-> a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto)
-> a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)
"""

venda = float(input('digite o valor da venda(R$): '))

venda_a_vista = venda - (venda * 0.10)
venda_parcelada = venda / 3
comissao_venda_a_vista = venda_a_vista * 0.05
comissao_venda_parcelada = venda * 0.05

print(f'total a pagar com desconto de 10% = R${venda_a_vista:.2f}')
print(f'parcelamento de 3x sem juros: valor da parcela = R${venda_parcelada:.2f}')
print(f'comissão do vendedor (venda a vista) = R${comissao_venda_a_vista:.2f}')
print(f'comissão do vendedor (venda parcelada) = R${comissao_venda_parcelada:.2f}')
