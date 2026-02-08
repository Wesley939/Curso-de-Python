'''
    Exercício Python #007 - Média Aritmética
'''

nota1 = float(input('Primeira nota do aluno: '))
nota2 = float(input('Segunda nota do aluno: '))

media = (nota1 + nota2) / 2

print(f'A media entra \033[1;4;36m{nota1:.2f}\033[m e \033[1;4;36m{nota2:.2f}\033[m é igual a \033[1;4;36m{media:.2f}\033[m')
