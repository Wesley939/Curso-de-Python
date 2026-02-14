# Faça um programa que leia um número qualquer e mostre o seu fatorial

# Ex:
# 5! = 1x2x3x4x5 = 120

# number = int(input("Digite o seu fatorial: "))

number = int(input("Digite o seu fatorial: "))
fatorial = 1
print(f"{number}! = ", end="")
while number > 0:
    fatorial *= number
    print(number, end= '')
    if number > 1:
        print('', end=" x ")
    number -= 1

# print()

print(f" = {fatorial}")
