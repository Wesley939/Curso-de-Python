"""
escreva um programa que leia um numero interio qualquer
e peça para o usuário escolher qual será a base de conversão:

1 -> para binario
2 -> para octal
3 -> para hexadecimal

"""
number = int(input('Digite um número inteiro: '))
print(''' Escolha uma das bases para conversão: 
[ 1 ] Converter para Binario
[ 2 ] Converter para Octal
[ 3 ] converter para Hexadecimal  ''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'{number} convertido para Binario é igual a  {bin(number)[2:]}')
elif opcao == 2:
    print(f'{number} Convertido para Octal é igual a {oct(number)[2:]}')
else:
    print(f'{number} Convertido para Hexadecimal é igual a {hex(number)[2:]}')