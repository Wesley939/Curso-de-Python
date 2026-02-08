"""

crie um programa que leia duas notas de um aluno e calcule a sua media,
mostrando uma mensagem final, de acordo com a media atingida:

>media abaixo de 5.0:
reprovado

>media entre 5.0 e 6.9:
recuperação

>media 7.0 ou superior:
aprovado

"""

nota1 = float(input("Digite a primeira nota: "))
print(f"Sua nota foi de {media:.2f} ")
if media >= 7.0:
    print("você foi \033[1;4;32mAprovado\033[m")
elif media >= 5.0:
    print("você ficou de \033[1;4;34mRECUPERAÇÃO\033[m")
else:
    print("você foi \033[1;4;31mREPROVADO\033[m")
