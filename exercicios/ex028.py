# Fazer um progrmaa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário descobrir qual foi o número escolhido pelo computador
# O programa deverá escrever na tela se o usuário ganhou ou venceu
import random
print("Vou pensar em um número entre 0 e 5 tente advinhar")
numero = int(input("Em que número eu pensei? "))
computador = random.randint(0,5)
if numero == computador:
    print("Você acertou! Parabéns!")
else:
    print("Ganhei! Eu pensei no número {} e não no {}" .format(computador,numero))
# print("Você acertou" if computador == numero else "Você errou")
