'''

Crie um programa que leia o nome completo de uma pessoa e mostre:

> O nome com todos as letras maiusculas e minusculas .
> Quantas letras ao todo (sem considerar espaços).
> Quantas letras tem o primerio nome.

'''
# lé o nome do usuario
nome = str(input('Digite seu nome completo: ')).strip()

print('Analisando seu nome...')
print(f'Seu nome em maiusculas é {nome.upper()}')
print(f'Seu nome em minusculas é {nome.lower()}')
print(f'Seu nome tem ao todos {len(nome) - nome.count(' ')} letras')

separa = nome.split()
print(f'Seu primeio nome é {separa[0]} ele tem {len(separa[0])}')
