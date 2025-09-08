# Melhore o jogo DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai advinhar até acertar, mostrando no final quantos palpites foram necessários para vencer
import random

print("Vou pensar em um número entre 0 e 5 tente advinhar")

numero = int(input("Em que número eu pensei? "))
computador = random.randint(0,5)
tentativas = 1

while numero != computador:
    numero = int(input("Errou!!! Digite outro número: "))
    tentativas += 1

print(f"O número era {computador}")
print(f"Você precisou de {tentativas} tentativas para vencer")
