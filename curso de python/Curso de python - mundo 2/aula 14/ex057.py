# Faça um programa que leia o SEXO  de uma pessoa, mas só aceite os valores ´M´ ou ´F´.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input("Informe seu sexo: [M/F]")).upper()
x = sexo

print(x)

while x != 'M' and x != 'F':
    teste = str(input("Dados inválidos. Por favor, informe seu sexo: ")).upper()
    x = teste
    print(f"foi digitado {x}")


# nb = ''
# while nb != 'F':
#     n = str(input('Digite ´F´ para finalizar: ')).upper()
#     nb = n