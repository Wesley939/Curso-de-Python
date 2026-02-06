'''
    faça um algoritmo que leia o preço de um produto e mostre seu
    novo preço, com %5 desconto.
'''

preco = float(input('Qual é o preço do produto? R$'))

desconto = preco * (5/100)
preco_final = preco - desconto

print(f'O produto que custava {preco:.2f}, na promoção com desconto  de %5 vai custar R${preco_final:.2f}')
