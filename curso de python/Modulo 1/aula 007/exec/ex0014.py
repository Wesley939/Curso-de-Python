'''
ESCREVA UMA PROGRAMA QUE CONVERTA UMA TEMPERATURA
DIGITADA EM °C E CONVERTA PARA °F
'''

temper = float(input('Informe a temperatura em °C: '))

conversor = (temper * 1.8) + 32

print(f'A temperatura de {temper}°C correspende a {conversor:.0f}°F')
