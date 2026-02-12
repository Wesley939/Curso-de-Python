#Crie um programa que leia DOIS VALORES e mostre MENU na tela:

#[1] somar 
#[2] multiplicar
#[3] maior
#[4] novos números
#[5] sair do programa

#Seu programa deverá realizar a operação solocitada em cado casa.


number2 = int(input("Segundo valor: "))
number1 = int(input("Segundo valor: "))
calculator = 0

while calculator != 5:

    print('''
        ------ MENU ------
        
        [ 1 ] SOMA
        [ 2 ] MULTIPLICAR
        [ 3 ] MAIOR
        [ 4 ] NOVOS NÚMEMOS
        [ 5 ] SAIR DO PROGRAMA
    ''')
    calculator = int(input(">>> Qual sua opição? "))

    if calculator == 1:
        soma = number1 + number2
        print(f"{number1} + {number2} = {soma}")
    
    elif calculator == 2:
        mult = number1 * number2
        print(f"{number1} * {number2} = {mult}")

    elif calculator == 3:
        if number1 > number2:
            print(f"O número {number1} é maior que o número {number2}")
        elif number2 > number1:
            print(f"O número {number2} é maior que o número {number1}")

    elif calculator == 4:
        print("Informe os novos números:")
        number2 = int(input("Segundo valor: "))
        number1 = int(input("Segundo valor: "))

    elif calculator == 5:
        print("Programa finalizado...")

    elif calculator >= 6:
        print("Operação invalida. Tente novamente")
        
        print('''
            ------ MENU ------

            [ 1 ] SOMA
            [ 2 ] MULTIPLICAR
            [ 3 ] MAIOR
            [ 4 ] NOVOS NÚMEMOS
            [ 5 ] SAIR DO PROGRAMA

              ''')
        calculator = int(input(">>> Qual sua opição? "))
        
        if calculator == 5:
            print("Programa finalizado...")

    print("="*50)
                                                                          
