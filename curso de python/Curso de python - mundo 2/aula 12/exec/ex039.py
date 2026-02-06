"""
Faça um programa que leia um ano de nacimento de um jovem e informe, de acordo com sua idade:

> se ele ainda vai se alistar ao serviço militar.
> Se a hora de se alistar.
> Se já passou do tempo do alistamento.

seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

from datetime import date

nasc = int(input("Ano de Nacimento: "))

anoAtual = date.today().year
idade = anoAtual - nasc 

print(f"Quem nasceu em {nasc} tem {idade} anos em {anoAtual}")

if idade == 18:
    print("Você tem que se Alistar \033[1;4;31mIMEDIATAMENTE\033[m")
elif idade < 18:
    saldo = 18 - idade
    alist = anoAtual + saldo
    print(f'Ainda faltam {saldo} anos para o alistamento')
    print(f'Seu alistamento será {alist}')
else:
    saldo = idade - 18
    alist = anoAtual - saldo 
    print(f'Você ja deveria ter se alistado há {saldo} anos')
    print(f'Seu alistamento foi a {alist}')