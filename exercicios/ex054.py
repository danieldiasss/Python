# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não antigiram a maioridade e quantas já são maiores.
from datetime import date
data_atual = date.today()
ano_atual = data_atual.year
mais_velho = 0
mais_novo = 0

for c in range (1,8):
    nascimento = int(input(f"Em que ano a {c}º pessoa nasceu? "))
    idade = (ano_atual-nascimento)
    if idade > 18:
        mais_velho += 1
    else:
        mais_novo += 1

print("Ao todo tivemos {} pessoas maiores de idade, e {} menores de idade" .format(mais_velho,mais_novo))