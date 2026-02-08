# Faça um programa que leia o PESO de CINCO PESSOAS.
# No final mostre qual foi o MAIOR e o MENOR peso lidos.

maior = 0
menor = 0

for pessoa in range(1, 6):
    peso = float(input(f"Peso da {pessoa}° pessoa: "))
    if pessoa == 1:
        maior = pessoa
        menor = pessoa
    else:
        if peso  > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f"O maior peso lido foi de \033[31m{maior}\033[mKg")
print(f"O menor peso lido foi de \033[32m{menor}\033[mKm")
