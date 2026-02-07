# Faça um programa que calcule a soma entre todos
# os NÚMEROS IMPARES que são múltiplos de três e que
# se encontram no intervalo de 1 até 500

for i in range(1, 501):
    if i % 2 == 1 and i % 3 == 0:
        soma = i * 3
        print(f'A soma dos impares multiplos de 3 entre 1 até 500: {soma}')
