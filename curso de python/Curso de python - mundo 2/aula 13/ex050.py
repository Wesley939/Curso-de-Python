# Desenvolva um programa que mostre leia SEIS NUMEROS INTEIROS
# e mostre a soma apenas daqueles que foram PARES.
# Se o valor digitado for IMPAR, desconsidere-o

soma = 0
for x in range(6):
    number = int(input(f"Digite o {x}, numero interio: "))
    if number % 2 == 0:
        soma += number
print(f"a soma dos numeros interios é {soma}")  