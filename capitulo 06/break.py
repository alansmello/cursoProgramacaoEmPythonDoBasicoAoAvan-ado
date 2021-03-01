"""
Saindo de Loops com break

Funciona da mesma forma que nas linguagens C ou Java.
Utilizamos o break para sair de loops de maneira projetada.
"""

#Exemplo 01

for number in range (1, 11):
    if number == 6:
        break
    else:
        print(number)
print('sair do Loop')


#Exemplo 02

while True:
    command = input("Digite 'sair' para parar: ")
    if command == 'sair':
        break
