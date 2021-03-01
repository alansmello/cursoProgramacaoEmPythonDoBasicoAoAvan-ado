"""
Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar
subindo a escada. Calcule e mostre quantos degraus o usuário deverá subir para atingir
seu objetivo.
"""
import math


degrau = float(input('digite a altura(cm) do degrau : '))
altura = float(input('digite a altura(cm) que deseja subir: '))

quantidade_degrau = altura / degrau

print(f'você deverá subir {math.ceil(quantidade_degrau)} degraus.')
