# Faça um programa que leia o NOME, IDADE e SEXO de 4 PESSOAS.
# No final do programa, mostre:

# A MÉDIA DE IDADE do grupo
# Qual é o nome do homem MAIS VELHO
# Quantas mulheres têm menos de 20 anos.

totalM = 0
somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
for pessoa in range(1, 5):
    print(f"----- {pessoa}° PESSOA -------")
    name = str(input("nome: ")).title()
    idade = int(input("idade: "))
    sexo = str(input("sexo [ M/F ]: "))
    somaidade += idade

    if pessoa == 1 and sexo in "Mm":
        nomeVelho = nome
        maiorIdadeHomem = idade

    if idade > idadeH and sexo in "mM":
        idadeH = idade
        nomeH = name
    if idade < 20 and sexo in "Ff":

        totalM += 1

mediaIdade = somaIdade / 4

print(f"A média de idade dos grupo é de {media:.1f} anos")
print(f"O homem mais velho tem {idadeH} anos e se chama {nomeH}")
print(
    f"O todo de mulheres com menos de 20 anos são {totalM} mulheres com menos de 20 anos"
)
