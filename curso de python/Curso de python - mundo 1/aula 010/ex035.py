"""

desenvolva um programa que leia o comprimento de três e diga ao usuário
se elas podem ou não formar um triâgulo

"""

print("-=" * 10)
print("Analizadador de Triangulos")
print("-=" * 10)

l1 = float(input("Primeiro segmento: "))
l2 = float(input("Segundo segmento: "))
l3 = float(input("Terceiro segmento: "))

if (l1 + l2 < l3) or (l2 + l3 > l1) or (l1 + l3 > l2):
    print("Os segmentos acima PODEM FORMAR triângulo")
else:
    print("Os segmentos acima NÃO PODEM FORMAR triâgulo")
