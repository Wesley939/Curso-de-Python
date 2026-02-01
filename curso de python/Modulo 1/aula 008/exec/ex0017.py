'''

faça um programa que leia o comprimento do cateto oposto
e do cateto adjacente de um triangulo retângulo, calcule e mostre o comprimento da hipotenusa.

'''
from math import hypot

oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))

hipotenusa = hypot(oposto, adjacente)

print(F'A hipotenusa  vai medir {hipotenusa:.2f}')
