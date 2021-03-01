"""
Faça um programa para ler as dimensões de um terreno (comprimento 'c' e largura 'l'), bem como o preço
do metro de tela 'p'. Imprima o custo para cercar este mesmo terreno com tela.
"""

comprimento = float(input('digite o comprimento do terreno em metros: '))
largura = float(input('digite a largura do terreno em metros: '))
tela = float(input('digite o preço do metro de tela(R$): '))

total_terreno = comprimento * 2 + largura * 2
custo_tela = total_terreno * tela

print(f'O valor total para cercar o terreno é R$ {custo_tela:.2f} .')
