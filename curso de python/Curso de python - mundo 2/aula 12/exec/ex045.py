"""

Crie um programa que faça o computador jogar
jokenpô com você

"""

from time import sleep
from random import randint

print(
    """ Suas opção: 
[ 0 ] PEDRA 
[ 1 ] PAPEL
[ 2 ] TESOURA
""",
    end="",
)
jogador = int(input("Qual sua jogada? "))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")

print("=-" * 30)

computador = randint(0, 2)

if computador == 0:
    print("Computador jogou PEDRA")
elif computador == 1:
    print("Computador Jogou PAPEL")
else:
    print("Computador Jogou TESOURA")

if jogador == 0:
    print("Jogador jogou PEDRA")
elif jogador == 1:
    print("Jogador Jogou PAPEL")
else:
    print("Jogador Jogou TESOURA")

print("=-" * 30)

if jogador == computador:
    print('EMPATE')
elif jogador  == 0 and computador == 2:
    print('JOGADOR VENCEU')
elif jogador == 1 and computador == 0:
    print('JOGADOR VENCEU')
elif jogador == 2 and computador == 1:
    print('JOGADOR VENCEU')
else:
    print('COMPUTADOR VENCEU')