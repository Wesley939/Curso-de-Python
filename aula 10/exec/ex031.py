"""

Desonvolva um programa que pergunte a distancia de uma viagem de KM.
calcule o preço da passagem, cobrando R$0,50 por KM para viagens de até 200KM
é R$0,45 para viagens mais longas.

"""

viagem = int(input("Qual é a distacia da sua viagem em KM? "))

if viagem <= 200:
    x = viagem * 0.50
    print(f"Sua viagem sera de {viagem}KM, o preço foi de {x}")
else:
    x = viagem * 0.45
    print(f"Sua viagem sera de {viagem}KM, o preço foi de {x}")
