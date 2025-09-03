# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
vel = int(input("Qual a velocidade do carro? "))
multa = (vel - 80) * 7
if vel >80:
    print("O valor da sua multa será {:.2f}R$" .format(multa) )
else:
    print("Você não foi multado")