'''

faça um programa que leia o nome completo de uma pessoa.
mostrando em seguida o primeiro e o último nome separadamente.

EX: Ana Maria de Sousa
primeiro = Ana
ultimo = souza

'''
nome = str(input('Digite seu nome completo: ')).strip().title()

n = nome.split()
print(f'primerio nome é {n[0]}')
print(f'segundo nome é {n[len(n)-1]}')
