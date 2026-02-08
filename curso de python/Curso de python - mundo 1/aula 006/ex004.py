'''
    DESAFIO 002
    Exercício Python #004 - Dissecando uma Variável

'''

n = input('Digite algo: ')

print(f'O tipo primitivo desse valor é \033[4;34m{type(n)}\033[m')
print(f'Só tem espaco? \033[4;34m{n.isspace()}\033[m')
print(f'É um número? \033[4;34m{n.isnumeric()}\033[m')
print(f'É alfabetico? \033[4;34m{n.isalpha()}\033[m')
print(f'É alfaNumérico? \033[4;34m{n.isalnum()}\033[m')
print(f'Esta em Maiusculo? \033[4;34m{n.isupper()}\033[m')
print(f'Esta em Minusculo? \033[4;34m{n.islower()}\033[m')
print(f'esta Centralizado? \033[4;34m{n.istitle()}\033[m')
