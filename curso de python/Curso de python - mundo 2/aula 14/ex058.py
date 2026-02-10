#Melhore o jogo do DESAFIO 028 onde o computador vai ´´´pensar´´ em um 
#NÚMERO ENTRE 0 E 10. Só que agora o jogador vai tentar adivinhar até acertar,
#mostrando no final quantos palpites foram necessários para vencer.






from random import randint

print("sou seu computador")
print("acabei de pensar em um numero emtre 0 e 10")
print("Sera que você consegue adivinhar")

user = int(input("Qual o seu palpite: "))

computer = randint(0,10)
counter = 0

while user != computer:
    print("Menos... Tente novamente mais uma vez.")
    user = int(input("Qual é seu palpite: "))
    counter += 1

print(f"acertou com {counter} tentativas. Parabéns. ")   