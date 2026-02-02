"""

escreva um programa para aprovar o emprestimo bancario para a compra de uma casa.
O programa vai pergunta o valor da casa, salario do comprador e em quantos anos 
ele vai pagar

Cacule o valor da prestacao mensal sabendo que ela nao pode exceder 30% do salario
ou entao o emprestimo se negado.

"""

casa = int(input("Qual o valor da casa: R$"))
salario = float(input("Qual o seu salario: R$"))
financiamento = int(input("Quantos anos Pretende financiar? "))

prestacao = casa / (financiamento * 15) 

porcentagemSalario = salario * 0.30

print(f"Para pagar uma casa de R${casa:.2f} em {financiamento} anos a prestação será de R${prestacao:.2f}")
if (porcentagemSalario > prestacao ):
	print("Emprestimo pode ser \033[1;4;32mCONCEDIDO\033[m")
else:
	print("Emprestimo \033[1;4;31mNEGADO!\033[m")