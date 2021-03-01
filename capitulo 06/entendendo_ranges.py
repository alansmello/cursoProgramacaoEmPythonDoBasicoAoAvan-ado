"""
Ranges
- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória,
mas sim de maneira específicada.

Formas gerais:
#Forma 1
range(valor_da_parada)
Obs: valos_da_parada não inclusive( início padrão 0, e passo de 1 em 1)

# Forma 2

range(valor_de_inicio, valor_de_parada)

Obs: valor_da_parada não inclusive( início especificado e passo de 1 em 1)

#Forma 3
range(valor_de_inicio, valor_de_parada, passo)

Obs: valor_da_parada não inclusive( início especificado e passo especificado)

#Forma 4 (Inversa)
range(valor_inicio, valor_parada, passo_decremento)

Obs: valor_da_parada não inclusive( início especificado e passo especificado)
"""

print('\n_________Forma 1__________\n')
for num in range(11):
    print(num)




print('\n_________Forma 2__________\n')
for num in range(1, 11):
    print(num)

print('\n_________Forma 3__________\n')

for num in range(1, 11, 2):
    print(num)

print('\n_________Forma 4__________\n')

for num in range(11, 0, -1):
    print(num)

