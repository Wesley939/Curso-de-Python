"""

Elabere um programa que calcule o valor a ser pago
por um produto, considerando o seu
preço normal e condição de pagamento:

> Á vista dinheiro/cheque:
        10% de desconto
> Á vista no cartão:
        5% de desconto
> Em ate 2x no cartão:
        preço normal
> 3x ou mais no cartão:
        20% de juros

"""

compra = float(input("Preço da Compras: R$"))
print(
    """ QUAL A FORMA DE PAGAMENTO?

[ 1 ] Á vista dinheiro/cheque
[ 2 ] Á vista no cartão
[ 3 ] Em ate 2x no catão
[ 4 ] 3x ou mais no cartão
"""
)
opcao = int(input("Qual Opção? "))

if opcao == 1:
    desconto = compra - (compra * (10 / 100))
    print(f"Sua Compra de R${compra:.2f} vai custar R${desconto:.2f} no final. ")

elif opcao == 2:
	desconto = compra - (compra * (5 / 100))
	print(f'Sua compra de R${compra:.2f} vai custar R${desconto} no final')

elif opcao == 3:
	parcela = compra / 2
	print(f'Sua compra sera pacelada em 2x de R${parcela:.2f} SEM JUROS ')
	print(f'Sua compra ficou no valor de R${compra:.2f} ') 
else:
	parcela = int(input('Quantas parcelas? '))
	juros = compra + (compra * (20 / 100))
	valorParcela = juros / parcela
	print(f'Sua compra sera parcela em {parcela}x de R${valorParcela:.2f} COM JUROS ')
	print(f'Sua compra de R${compra:.2f} vai custar R${juros:.2f}')