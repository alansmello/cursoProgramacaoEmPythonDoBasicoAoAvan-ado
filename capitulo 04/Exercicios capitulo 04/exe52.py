"""
Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor que cada um
deu para a realização da aposta. Faça um programa que leia quanto cada apostador investiu, o valor do prêmio, e
imprima quanto cada um ganharia do prêmio com base no valor investido.
"""

jogador_a = float(input('digito quanto o jogador A investiu para a aposta (R$): '))
jogador_b = float(input('digito quanto o jogador B investiu para a aposta (R$): '))
jogador_c = float(input('digito quanto o jogador C investiu para a aposta (R$): '))
premio = float(input('digite o valor do prêmio: '))

valor_aposta = jogador_a + jogador_b + jogador_c
percentual_jog_a = jogador_a / valor_aposta
percentual_jog_b = jogador_b / valor_aposta
percentual_jog_c = jogador_c / valor_aposta

print(f'O jogador A levará o total de R$ {(premio * percentual_jog_a):.2f}')
print(f'O jogador B levará o total de R$ {(premio * percentual_jog_b):.2f}')
print(f'O jogador C levará o total de R$ {(premio * percentual_jog_c):.2f}')
