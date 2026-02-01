nome = str(input("Qual o seu nome completo")).strip()
nome = nome.title()
silva = 'Silva' in nome

print(f'Seu nome tem Silva? {silva}')
