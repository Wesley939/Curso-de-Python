# Faça um programa que mostre na tela uma CONTAGEM regreciva para
# o estouro de fogos de artificio, indo de 10 até 0
# com uma pausa de 1 segundo
import time

for c in range(10, -1, -1):
    print(c)
    time.sleep(1)
print('BUM! BUM POOW!')