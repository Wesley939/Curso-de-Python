'''

Faça um programa que leia um numero de 0 a 9999 e mostre na tela
cada um dos digitos separados.
Ex:
Digite um numero: 1834
unidade: 4 desena: 3 centena: 8 milhar: 1

'''

num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Analizando o número {num}')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'milhar: {m}')
