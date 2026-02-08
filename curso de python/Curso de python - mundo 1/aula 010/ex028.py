"""

Escreva um programa que faça o computador "pensar" em um número entre 0 e 5 e peça para o
usario tentar descobrir qual foi o número escolido pelo computador.

O programa deverá escrever na tela se o usuario venceu ou perdeu.

"""

from random import randint
from time import sleep

print("-=-" * 30)
print("Vou pensar em um número entre  0 e 5. tente adivinhar...")
print("-=-" * 30)

pensei = int(input("Em que número eu estou pendo? "))

computador = randint(0, 5)

print("\033[1;31mPENSANDO ...\033[m")
sleep(3)

if pensei != computador:
    print(f"\033[1;32mGANHEI\033[m! Eu pensei no número {computador} e não no {pensei}")
else:
    print(f"\033[32mVOCÊ GANHOU!\033[m você pensou no mesmo número que eu ")
