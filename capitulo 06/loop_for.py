"""
Loop for
Loop -> Estrutura de repetição.
For -> Uma dessas estruturas

Python
for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:
- Strings
    nome = 'Geek University'
- Listas
    lista = [1, 3, 5, 7, 9]
Range
    numeros = range(1, 10)
"""

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) #temos que transformar em uma lista

#Exemplo de for 1 (Iterando em uma String)

for letra in nome:
    print(letra)

#Exemplo de for 2 (Iterando sobre uma Lista)

for num in lista:
    print(num)


#Exemplo de for 3 (Iterando sobre um Range)
"""
Range(valor_inicial, valor_final)
Obs:  valor final não é incluso.
"""

for num in range(1, 10):
    print(num)

#Exemplo de for 4 (enumerate)

#((0, 'G'), (1, 'e'), (3, 'e'), (4, 'k'), (5, ' '), (6, 'U')...)

for valor in enumerate(nome):
    print(valor)

# obs: quando não precisamos de um valor, podemos descartá-lo utilizando um underline(_)
for _, letra in enumerate(nome):
    print(letra)

#outros exemplos

qtd = int(input('Quantas vezes esse loop deve rodar: '))
soma = 0
for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')



for letra in nome:
    print(letra, end='')

"""
Tabela de emojis -> https://apps.timwhitlock.info/emoji/tables/unicode
Original -> U+1F602
Modificado -> U0001F602
"""
print('\U0001F602')
for num in range(1,11):
    print('\U0001F602' * num)
