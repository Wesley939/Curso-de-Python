'''
    faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario,
    com 15% de aumento.
'''

salario_atual = float(input('Qual o salario do funcionario? R$'))

percentual_aumento = 1 + 15/100
novo_salario = salario_atual * percentual_aumento

print(f'Um funcionario que ganhava R${salario_atual}, com 15% de aumento, passa a receber R${novo_salario:.2f}')
