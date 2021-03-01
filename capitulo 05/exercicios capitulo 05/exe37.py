"""
As tarifas de certo parque de estacionamento são as seguintes:
* 1ª e 2ª hora - R$1,00 cada
* 3ª e 4ª hora - R$1,40 cada
5ª hora e seguintes - R$2,00 cada

O número de horas a pagar é sempre inteiro e arredondado por excesso.
Deste modo, quem estacionar durante 61 minutos pagará por duas horas,
que é o mesmo que pagaria se tivesse permanecido por 120 minutos. Os
momentos de chegada ao parque e partida deste são apresentados na forma
de pares de inteiros, representando horas e minutos. Por exemplo, o par
de 12 50 representará "dez para uma da tarde". Pretende-se criar um
programa que, lidos pelo teclado os momentos de chegada e de partida,
escreva na tela o preço cobrado pelo estacionamento. Admite-se que a
chegada e a partida se dão com intervalo não superior a 24 horas.
Portanto, se uma dada hora de chegada for superior à da partida, isso
não é uma situação de erro, antes significará que a partida ocorreu
no dia seguinte ao da chegada.
"""
import math
hora_chegada = int(input('digite a hora de chegada: '))
minuto_chegada = int(input('digite os minutos de chegada: '))

hora_saida = int(input('digite a hora de saida: '))
minuto_saida = int(input('digite os minutos de saida: '))

if hora_saida <= hora_chegada:
    total_minutos_saida = (24 + hora_saida) * 60 + minuto_saida

else:
    total_minutos_saida = hora_saida * 60 + minuto_saida

total_minutos_chegada = hora_chegada * 60 + minuto_chegada

minutos_que_ficou = math.ceil((total_minutos_saida - total_minutos_chegada) / 60)

if minutos_que_ficou <= 2:
    print(f'Total a pagar: R${minutos_que_ficou * 1.00:.2f}')
elif 3 <= minutos_que_ficou <= 4:
    print(f'Total a pagar: R${minutos_que_ficou * 1.40:.2f}')
else:
    print(f'Total a pagar: R${minutos_que_ficou * 2.00:.2f}')
