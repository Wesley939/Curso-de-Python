# -*- coding: utf-8 -*-
"""

escreva um programa que leia dois numeros inteiros e compare-se,
mostrando na tela uma mensagem:

> O primeiro valor é Maior
> O segundo valor é Maior
> Não existe um valor Maior, os dois são iguais

"""
number1 = int(input('Digite o primerio valor: '))
number2 = int(input('Digite o segundo valor: '))

if number1 > number2 :
    print('O primero valor é maior')
elif number1 == number2 :
    print('Não existe um valor maior ambos os valores são iguais ')
else:
    print('O segundo numero é maior')