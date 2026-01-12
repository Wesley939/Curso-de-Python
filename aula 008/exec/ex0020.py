'''

O mesmo professor do desafio anterior
quer sortear a ordem de presentação de
trabalho dos alunos. faça um programa que leia
o nome dos quatro alunos e mostre a ordem de sorteada.

'''
from random import shuffle

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('terceiro aluno: ')
n4 = input('Quarto Aluno: ')

lista = [n1, n2, n3, n4]

shuffle(lista)
print('A ordem de apresentação sera')
print(lista)