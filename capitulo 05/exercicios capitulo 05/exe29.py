"""
Faça uma prova de matemática para crianças que estão aprendendo a somar números inteiros menores que 100.
Escolha números aleatórios entre 1 e 100, e mostre na tela a pergunta: qual é a soma de a + b, onde a e b
são os números aleatórios. Peça a resposta. Faça cinco perguntas ao aluno, e mostre para ele as perguntas
e as respostas corretas, além de quantas vezes o aluno acertou.
"""
import random

pergunta = 1
acerto = 0
respostas_certas = []

while pergunta <=5:
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    resposta = int(input(f'qual é a soma de {a} + {b}? '))
    respostas_certas.append(f'soma de {a}+{b} = {a+b}')
    if resposta == (a+b):
        acerto += 1
    pergunta += 1
print('\nRespostas certas:')

for i in range(5):
    print(respostas_certas[i])

print(f'\nVocê acertou {acerto} perguntas.')
