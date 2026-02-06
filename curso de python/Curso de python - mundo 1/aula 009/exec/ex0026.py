'''
faça um programa que leia uma frase pelo teclado e mostre:

 >Quantas vezes aparece a letra 'A'
>Em que pisição ela aparece a primeira vez.
>Em que posição ela aparecea última vez.

'''

frase = str(input('Digite uma frase: ')).strip().upper()

print(f'A frase analisada foi {frase}')
print(f'A letra A apareces {frase.count("A")} vezes na frase.')
print(f'A primeira letra A apareceu na pisição {frase.find("A")+1}')
print(f'A ultima letra A apareceu na posição {frase.rfind("A")+1}')
