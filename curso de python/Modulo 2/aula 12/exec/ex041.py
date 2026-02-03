"""

A confederação nacional de natação precisa de programa que leia o ano 
de anacimento de um atleta e mostre sua categoria, de acordo com a idade.

> Até 9 anos: Mirim
> Até 14 anos: Infantil
> Até 19 anos: Junior 
> Até 20 anos: Sênor
> Acima: master 

"""
from datetime import date

nasc = int(input('Qual seu ano de nascimento? '))

idade = date.today().year - nasc

print('CATEGORIA:')
if idade <= 9 :
    print(f'Você tem {idade} anos sua categoria é Mirim')
elif idade <= 14 :
    print(f'Você tem {idade} anos sua categoria é Infantil')
elif idade <= 19 :
    print(f'Você tem {idade} anos sua categoria é Junior')
elif idade <= 20 :
    print(f'Você tem {idade} anos sua categoria é Sênor')
else:
    print(f"Você tem {idade} anos sua categoria é Master")