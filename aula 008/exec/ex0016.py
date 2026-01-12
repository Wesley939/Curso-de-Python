'''

crie um programa que leia um número real
qualquer pelo teclado e mostra na tela
a sua posição anterios

EX:
digite um numero: 6.127
o numero 6.127 tem a parte inteira 6.

'''
from math import trunc

number = float(input('Digite um numero real: '))
inteiro =  trunc(number)
print(f'o numero {number} tem a parte inteira {inteiro}.')
