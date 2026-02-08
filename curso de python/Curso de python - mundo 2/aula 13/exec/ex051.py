# Desenvolva um programa que leia o PRIMEIRO TERMO e a RAZÃO
# de uma PA no final, mostre os 10 
# primeiro termos desse progressão

termo = int(input('Primeiro numero: '))
razao = int(input('Razão: '))
decimo = termo + (10 - 1) * razao

for x in range(termo, decimo + razao, razao):
    print(f'{x}',end=' -> ')
print('ACABOU')