'''
    DESAFIO 002
    Exercício Python #004 - Dissecando uma Variável

'''

n = input('Digite algo: ')

print('O tipo primitivo desse valor é {}'.format(type(n)))
print('Só tem espaco? {}'.format(n.isspace()))
print('É um número? {}'.format(n.isnumeric()))
print('É alfabetico? {}'.format(n.isalpha()))
print('É alfaNumérico? {}'.format(n.isalnum()))
print('Esta em Maiusculo? {}'.format(n.isupper()))
print('Esta em Minusculo? {}'.format(n.islower()))
print('esta Centralizado? {}'.format(n.istitle()))
