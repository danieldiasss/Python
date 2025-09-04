#  Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

# – Se ele ainda vai se alistar ao serviço militar.
# – Se é a hora de se alistar.
# – Se já passou do tempo do alistamento.

# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

data_atual = date.today()
ano_atual = data_atual.year

ano_nas = int(input("Digite o ano de nascimento: "))

idade = ano_atual - ano_nas

if idade == 18:
    print("Hora de se alistar")
elif idade > 18:
    print(f"Você precisa se alistar, passou {idade-18} anos do prazo") 
else:
    print(f"Falta {18-idade} anos para você se alistar")