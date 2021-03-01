"""
PEP8 - Python Enhancement Proposal
São propostas de melhorias para a linguagem Python

The Zen of Python

import this

A ideia da PPEP8 é que possamos escrever códigos Python de forma Pythônica.

[1] - Utilize Camel Case para nomes de classes;

    class Calculator:
        pass


    class ScientificCalculator:
        pass

[2] - Utilize nomes em minusculo separados por '_' para funções ou variáveis;

    def soma():
        pass


    def soma_two():
        pass

[3] - Utilize 4 espaços para identação ! (obs:não utilizar TAB, já que é configurável pra computadores diferentes.)

    if 'a' in 'banana':
        print('tem')


[4] -  Linhas em branco.

    * separar funções e definições de classes com 2 linhas em branco;
    * métodos dentro de uma classe deve ser separado por apenas uma linha em branco;

[5] - Imports devem ser sempre feitos em linhas separadas;

    # Import Errado:
    import sys, os

    # Import Certo
    import sys
    import os

    # Não há problema em utilizar:
    from types import StringType, ListType

    # Caso tenham muitos imports de um mesmo pacote, recomendasse fazer assim:
    from types import (
        StringType,
        ListType,
        SetType,
        OutroType
        )

    #Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentarios ou docstrigs e antes de constantes ou variáveis globais.


[6] - Espaços em expressões e instruções:

    #Não faça:

        funcao( algo[ 1 ], { outro: 2 })

        algo (1)

        dict ['chave'] = list [indice]

        x              = 1
        y              = 3
        variavel_longa = 5

    #Faça:

        funcao(algo[1], {outro: 2})

        algo(1)

        dict['chave'] = lista[indice]

        x = 1
        y = 3
        variavel_longa = 5

[7] - Termine sempre uma instrução com uma nova linha.


"""


import this
