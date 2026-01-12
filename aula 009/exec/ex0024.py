cidade = str(input('Em que cidade você nasceu? ')).strip()
cidade = cidade.title()
teste = cidade[:5] == 'Santa'
print(teste)
