"""

Escreva um programa que leia a velocidade de um carro.

Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi cultado.

A multa vai custar R$7,00 por cada KM acima do limite.

"""

velocidade = int(input("Qual é a sua velocidade atual do carro? "))
multa = (velocidade - 80) * 7

if velocidade >= 80:
    print("MULTADO! Você execeu o limite permitido que é de 80km")
    print(f"Você deve pagar uma multa de R${multa}!")
else:
    print("Tenha um bom dia! Dirija com seguraça!")
