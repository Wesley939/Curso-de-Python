# Exercício Python #008 - Conversor de Medidas

metro = float(input('Uma distancia em metros: '))

km = metro / 1000
hm = metro / 100
dam = metro / 10
dm = metro * 10
cm = metro * 100
mm = metro * 1000

print(f'A media  de \033[1;4;31m{metro:.1f}m\033[m coresponde a ')
print(f'\033[1;4;31m{km}km')
print(f'{hm}hm')
print(f'{dam}dam')
print(f'{dm:.0f}dm')
print(f'{cm:.0f}cm')
print(f'{mm:.0f}mm\033[m')
