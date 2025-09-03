# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
viagem = int(input("Digite a distância da viagem: "))
if viagem > 200:
    print("O valor da passagem é {:.2f} R$" .format(viagem*0.45))
else:
    print("O valor da viagem é {:.2f} R$"   .format(viagem*0.5))