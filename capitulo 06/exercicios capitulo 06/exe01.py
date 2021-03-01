"""
Faça um programa que determine e mostre os cinco primeiros múltiplos de 3,
considerando números maiores que 0.
"""
cont = 0
for number in range(1, 50):
    if (number % 3) == 0:
        print(f'{number} é divisivel por 3')
        cont += 1
    elif cont == 3:
        break
    else:
        print(number)
