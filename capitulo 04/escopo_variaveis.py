"""
Escopo de Variáveis

Dois casos de escopo:

1 - Variáveis Globais;
    São reconhecidas, ou seja, seu escopo compreende todo o programa.

2 - Variáveis Locais
    São reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
    está limitado ao bloco onde foi declarada.

Para declarar varáveis em Python fazemos:

    nome_da_variavel = valor_da_variavel

Obs.: Python é uma linguagem de tipagem dinâmica, assim sendo, ao declarar uma variável, não é necessário
colocar o tipo de dado dela.
"""

numero = 42
print(numero)
print(type(numero))