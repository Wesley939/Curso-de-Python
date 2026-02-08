# Crie um programa que leia uma FRASE qualquer e diga se ela
# é um POLINDROMO, desconsiderando, os espaços


frase = str(input("Escreva uma frase: ")).strip().upper()
palavra = frase.split()
junto = "".join(palavra)
inverso = ""

for i in range(len(frase) -1, -1, -1):
     inverso += frase[i]

print(f'O inverso de {junto} e {inverso}')

if inverso == frase:
    print('essa frase forma um POLINDROMO')
else:
    print('essa frase não forma um POLINDROMO')