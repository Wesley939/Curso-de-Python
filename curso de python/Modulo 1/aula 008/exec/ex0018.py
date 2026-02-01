'''

faça um programa que leia um ângulo
qualquer e mostre na tela o valor do seno
cosseno  e tangente desse ângulo

'''
import math

angulo = int(input('Digite o angulo que voçê deseja: '))

seno = math.sin(math.radians(angulo))
print(f'O ângulo de {angulo} tem o valor de {seno:.2f}.')

cosseno = math.cos(math.radians(angulo))
print(f'O ângulo de {angulo} tem o valor de {cosseno:.2f}.')

tangente = math.tan(math.radians(angulo))
print(f'O ângulo de {angulo} tem o valor de {tangente:.2f}')
