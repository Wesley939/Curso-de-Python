"""

Escreva um programa que pergute o salário de um funcionário e calcule o valor do seu aumento

Para salarios superiores a 1.250,00, calcule um aumento de 10%.

Para os inferiores ou aguais, o aumento é de 15%.

"""

salario = float(input("Qual é o salario do funcionario? R$"))

if salario <= 1250:
    novo_salario = ((15 / 100) * salario) + salario
    print(f"Quem ganhava R${salario:.2f} agora passa a ganha R${novo_salario}")
else:
    novo_salario = ((15 / 100) * salario) + salario
    print(f"Quem ganha R${salario:.2f} agora passa a ganha R${novo_salario:.2f}")
