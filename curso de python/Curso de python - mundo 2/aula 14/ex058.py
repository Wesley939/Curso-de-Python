# Melhore o jogo do DESAFIO 028 onde o computador vai ´´´pensar´´ em um
# NÚMERO ENTRE 0 E 10. Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint

print('Sou seu computador ...')
print('acabei de pensar em um numeros de 0 a 10.')
print('sera que voce consegue adivinhar?')

computer = randint(0, 10)
counter = 0

heGotItRight = False

while not heGotItRight:
    user = int(input('Qual é seu palpite? '))
    counter += 1
    if user == computer:
        heGotItRight = True
    else:
        if user > computer:
            print("Menos...")
        elif user < computer:
            print("Mais...")
print(f"Acertou com {counter} tentativas. Parabens!")
