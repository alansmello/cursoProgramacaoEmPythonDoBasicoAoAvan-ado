"""
Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação
escolhida. Escreva uma mensagem de erro se a opção for inválida.
Escolha a opção:
1- Soma de 2 números.
2- Diferença entre 2 números(maior pelo menor).
3- Produto entre 2 números.
4- Divisão entre 2 números (o denominador não pode ser zero).

"""
print ('Escolha a opção:\n')
print ('1- Soma de 2 números.')
print('2- Diferença entre 2 números(maior pelo menor).')
print('3- Produto entre 2 números.')
print('4- Divisão entre 2 números (o denominador não pode ser zero).')
opcao = int(input('\nDigite a opção desejada: '))


if opcao == 1:
    num1 = int(input('digite o primeiro numero: '))
    num2 = int(input('digite o segundo numero: '))
    print(f'A soma dos números é igual a {num1 + num2} .')
elif opcao == 2:
    num1 = int(input('digite o primeiro numero: '))
    num2 = int(input('digite o segundo numero: '))
    if num1 > num2:
        print(f'A diferença dos números é igual a {num1 - num2} .')
    else:
        print(f'A diferença dos números é igual a {num2 - num1} .')
elif opcao == 3:
    num1 = int(input('digite o primeiro numero: '))
    num2 = int(input('digite o segundo numero: '))
    print(f'O produto dos números é igual a {num1 * num2} .')
elif opcao == 4:
    numerador = int(input('digite o numerador: '))
    denominador = int(input('digite o denominador: '))
    if denominador == 0:
        print('o denominador não pode ser igual a zero.')
    else:
        print(f'O produto dos números é igual a {numerador / denominador} .')
else:
    print('Opção inválida.')
