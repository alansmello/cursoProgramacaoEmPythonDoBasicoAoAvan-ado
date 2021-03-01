"""
A importância de R$780.000,00 será dividida entre três ganhadores de um concurso.
Sendo que da quantia total:
* O primeiro ganhador receberá 46%;
* O segundo receberá 32%;
* O terceiro receberá o restante;
Calcule e imprima a quantia ganha por cada um dos ganhadores.

"""

premio = 780_000

ganhador1 = premio * 0.46
ganhador2 = premio * 0.32
ganhador3 = premio * (1 - 0.46 - 0.32)

print(f'o primeiro ganhador vai levar R${ganhador1:.2f}, o segundo R${ganhador2:.2f} e o terceiro R${ganhador3:.2f} .')
