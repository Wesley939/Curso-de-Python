import math

number = int(input('Digite um número: '))

print(f'O dobro de {number} vale {number**2}.')

print(f'O triplo de {number} vale {number**3}.')

raiz = math.sqrt(number)
print(f'\033[1;31;43mA raiz quadrada de {number} é igual a {raiz:.2f}.\033[m')
