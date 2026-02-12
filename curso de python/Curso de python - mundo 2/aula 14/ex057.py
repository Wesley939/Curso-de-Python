# Faça um programa que leia o SEXO  de uma pessoa, mas só aceite os valores ´M´ ou ´F´.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

generoPessoa = str(input("Digite seu genero: [M/F]")).upper()

while generoPessoa not in 'MF':
    print("Genero que foi digita esta errado;")
    generoPessoa = str(input("Digite o genero navamente: [M/F]")).upper()
