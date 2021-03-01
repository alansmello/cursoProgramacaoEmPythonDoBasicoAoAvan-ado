"""
Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triângulo
e, se forem, se é um triângulo escaleno, equilátero ou isóscele, considerando os seguintes
conceitos:
* O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados.
* Chama-se equilátero o triângulo que tem três lados iguais.
* Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
* Recebe o nome de escaleno o triângulo que tem os três lados diferentes.
"""
lado1 = float(input('entre com valor (cm) do lado 01 do triangulo: '))
lado2 = float(input('entre com valor (cm) do lado 02 do triangulo: '))
lado3 = float(input('entre com valor (cm) do lado 03 do triangulo: '))

if lado1 < (lado2 + lado3) and lado2 < (lado1 + lado3) and lado3 < (lado1 + lado2):
    if lado1 == lado2 == lado3:
        print('trata-se de um triangulo equilatero.')
    if lado1 == lado2 != lado3 or lado1 == lado3 != lado2 or lado2 == lado3 != lado1:
        print('trata-se de um triangulo isosceles.')
    if lado1 != lado2 != lado3:
        print('trata-se de um triangulo escaleno')
else:
    print('nao eh um triangulo!')
