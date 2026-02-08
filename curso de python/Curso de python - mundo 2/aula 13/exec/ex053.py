# Crie um programa que leia uma FRASE qualquer e diga se ela 
# é um POLINDROMO, desconsiderando, os espaços

 
frase = str(input("Escreva uma frase: "))
nova_frase = ''

for i in range(len(frase), 0, -1):
    print(frase[i])

if frase == frase:
    print('ok')
else:
    print('false')