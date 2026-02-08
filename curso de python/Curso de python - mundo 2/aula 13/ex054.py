# Crie um programa que leia o  ANO DE ANASCIMENTO de SETE PESSOAS. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

atual = date.today().year

print(atual)
maior = 0
menor = 0
for x in range(7):
    ano = int(input(f"Em que ano a {x} você nasceu? "))
    idade = atual - ano
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f"Ao todo tivemos {maior} pessoas maiores de idade")
print(f"E também tivemos {menor} pessoas menores de idade")
