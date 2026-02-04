"""

Refaça o desafio 035 dos Triângulos, 
acrescentando o recurso de mostrar que tipo de Triânguloss sera formado.

> EQUILATERO: todos os landos iguais
> ISÓSCELES: dois landos iguais
> ESCALENO: todos os landos sao diferentes

"""

a = int(input('Digite o primeiro lado do triangulo: '))
b = int(input('Digite o segundo lado do triangulo: '))
c = int(input('Digite o terceiro lado do triangulo: '))

if b == a and b == c:
    print('isso forma um triangulo EQUILATERO')
elif c == a or c == b:
    print('Dois lados de um triangulo formam um triangulo ISÓSCELES')    
else:
    print('Todos os lados do triangulo sao diferentes e isso forma um triangulo ESCALENO ')