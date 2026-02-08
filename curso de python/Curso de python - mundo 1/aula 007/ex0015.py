'''

Escreva um programa que pergunte a quantidade de KM
percorridos por um carro alugado e a quantidade de dias pelos
pelos quais ele foi alugado. Calcule o preco a pagar, sabendo que o carro
custa R$60 por dia e R$0,15 por KM rodados.q

'''

aluguel_diario = int(input('Quantos dias alugados? '))
km = float(input('Quantos KM rodados? '))

pagar = (aluguel_diario * 60) + (km * 0.15)

print(f'O total a pagar é de R${pagar:.2f}')
