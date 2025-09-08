# Crie um programa que leia dois valores e mostra um menu na tela:

# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa

# Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
menu = 0
while menu != 5:
    menu = int(input('''
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
'''))
    if menu == 1:
        print(f"A soma dos números é {n1+n2}")
    elif menu ==2:
        print(f"A multiplicação dos números é {n1*n2}")
    elif menu ==3:
        if n1>n2:
            print(f"O maior número é {n1}")
        elif n2>n1:
            print(f"O maior número é {n2}")
        else:
            print("Os dois valores são iguais")
    elif menu == 4:
        print("Informe os valores novamente")
        n1 = int(input("Digite um valor: "))
        n2 = int(input("Digite outro valor: "))
    elif menu == 5:
        print("FIM")

else:
    print("Opção inválida, tente novamente.")