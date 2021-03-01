"""
Loop while

Forma geral

while expressão_booleana:
    // execução do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira.

obs: Expressão booleana é toda expressão em que o resultado é verdadeiro ou falso.
Exemplo:
num = 5
num < 5
"""
#exemplo 01:

number = 1

while number <= 10:
    print(number)
    number += 1


#Obs: Em um loop while é importante que cuidemos do critério de parada, para não causar um loop infinito.

#Exemplo 02

resposta = ''

while resposta != 'sim':
    resposta = input('Já acabou Alan? :')
