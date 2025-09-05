# Crie um programa que faça o computador jogar Jokenpô com você. 
# pedra ganha de tesoura
# papel ganha de pedra
# tesoura ganha de papel

# import time
# import random
# print("Vamos brincar de Jokenpô ")
# print("-=-" * 30)
# time.sleep(1)

# jokenpo =["pedra", "papel", "tesoura"]
# jogador = str(input("Escolha entre papel,pedra,tesoura: ")).lower()
# computador = random.choice(jokenpo)

# print(f"Eu escolhi {computador}")
# time.sleep(1)
# if computador == "pedra" and jogador =="tesoura":
#     print("Você perdeu!!!")
# elif computador == "papel" and jogador == "pedra":
#     print("Você perdeu!!!")
# elif computador == "tesoura" and jogador == "papel":
#     print("Você perdeu!!!")
# elif computador == jogador:
#     print("Empatamos...")
# else:
#     print("Você ganhou")

from random import randint

itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)

print(''' Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

jogador = int(input("Qual é sua jogada? "))

if jogador < 0 or jogador > 2:
    print("Opção inválida!")
else:
    print("-=" * 11)
    print("O computador jogou {}".format(itens[computador]))
    print("O jogador jogou {}".format(itens[jogador]))
    print("-=" * 11)

    if computador == jogador:
        print("EMPATE!!!")

    elif computador == 0:  
        if jogador == 1:
            print("JOGADOR VENCE")
        elif jogador == 2:
            print("COMPUTADOR VENCE")

    elif computador == 1:  
        if jogador == 0:
            print("COMPUTADOR VENCE")
        elif jogador == 2:
            print("JOGADOR VENCE")

    elif computador == 2:  
        if jogador == 0:
            print("JOGADOR VENCE")
        elif jogador == 1:
            print("COMPUTADOR VENCE")



