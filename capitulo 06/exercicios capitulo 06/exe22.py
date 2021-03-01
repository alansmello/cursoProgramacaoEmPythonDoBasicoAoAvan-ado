"""
Escreva um programa completo que permita a qualquer aluno introduzir, pelo teclado,
uma sequencia arbitrária de notas(válidas no intervalo de 10 a 20) e que mostre na
tela, como resultado, a correspondente média aritmética. O número de notas com que
o aluno pretenda efetuar o cálculo não será fornecido ao programa, o qual terminará
quando for introduzido um valor que não seja válido como nota de aprovação.
"""
nota = 10
soma = 0
cont = 0
while 10 <= nota <= 20:
    nota = (int(input('digite uma nota: ')))
    if 10 <= nota <= 20:
        soma += nota
        cont += 1

print(f'A média dos valores válidos é igual a {(soma / cont):.2f} .')
