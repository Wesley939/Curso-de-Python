# Refaça o DESAFIO 009, mostrando a tabuada de um número
# que o usuario escolher, só que agora utilisando um LAÇO FOR

tabu = int(input("Qual tabuada você quer? "))

for c in range(11):
    print(f"{ tabu } x { c } = { tabu * c }")
