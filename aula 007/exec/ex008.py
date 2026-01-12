# Exercício Python #008 - Conversor de Medidas

metro = float(input('Uma distancia em metros: '))

km = metro / 1000
hm = metro / 100
dam = metro / 10
dm = metro * 10
cm = metro * 100
mm = metro * 1000

print('A media  de {:.1f}m coresponde a '.format(metro))
print('{}km'.format(km))
print('{}hm'.format(hm))
print('{}dam'.format(dam))
print('{:.0f}'.format(dm))
print('{:.0f}cm'.format(cm))
print('{:.0f}mm'.format(mm))
