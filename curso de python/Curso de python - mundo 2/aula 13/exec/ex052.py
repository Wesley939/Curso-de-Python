# Faça um programa que leia NÚMERO INTEIRO e diga se ele é
# ou não um NÚMERO PRIMO


number = int(input("Digite um número: "))

counter = 0
for i in range(1, number + 1, 1):
    if number % i == 0:
        print("\033[32m", end=" ")
        counter += 1
    else:
        print("\033[m", end=" ")
    print(f"{i}\033[m", end="")
print(' ')
print(f"O número {number} foi divisivel {counter} vezes.")
if counter == 2:
    print(f"O número {number} é um número par")
else:
    print(f'o número {number} não um número')