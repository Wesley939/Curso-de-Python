"""

Faça um programa que leia três números e mostre qual é o MAIOR e qual é o MENOR.

"""

a = int(input("Primeiro Valor: "))
b = int(input("Segundo Valor: "))
c = int(input("Terceiro Valor: "))

# Verificando quem é menor
menor = a  # suponho que o menor é o a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# Verificando quem é o mairo
maior = a

if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f"O menor valor digitado é {menor}")
print(f"O maior valor digitado é {maior}")
