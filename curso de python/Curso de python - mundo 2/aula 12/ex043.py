"""

Desenvolva uma logica que leia o peso e autura de uma pessoa, calcule seu IMC e mostre
seu status de acordo com a tabela abaixo:

> Abaixo de 18.5: 
	Abaixo do peso
> Entre 18.5 e 25:
	peso ideal
> 25 ate 30:
	sobre peso
> 30 ate 40:
	Obesidade 
> acima de 40
	Obesidade Mórbida
"""
altura = float(input('Qual sua altura: '))
peso = float(input('Qual o seu peso: '))

imc = peso / (altura ** 2)

print(f'seu IMC é {imc:.2f}')

if imc <= 18.5:
	print('Abaixo do peso')
elif imc <= 25:
	print('Peso ideal')
elif imc <= 30:
	print('Sobre peso')
elif imc <= 40:
	print('Obesidade')
else:
	print('Obesidade Mórbida')