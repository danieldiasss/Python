# Crie um programa que faça o computador jogar Jokenpô com você. 
# pedra ganha de tesoura
# papel ganha de pedra
# tesoura ganha de papel

import time
import random
print("Vamos brincar de Jokenpô ")
print("-=-" * 30)
time.sleep(1)

jokenpo =["pedra", "papel", "tesoura"]
jogador = str(input("Faça sua escolha: ")).lower()
computador = random.choice(jokenpo)

print(f"Eu escolhi {computador}")
time.sleep(1)
if computador == "pedra" and jogador =="tesoura":
    print("Você perdeu!!!")
elif computador == "papel" and jogador == "pedra":
    print("Você perdeu!!!")
elif computador == "tesoura" and jogador == "papel":
    print("Você perdeu!!!")
elif computador == jogador:
    print("Empatamos...")
else:
    print("Você ganhou")
