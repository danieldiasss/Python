#  A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JUNIOR
# – Até 20 anos: SÊNIOR
# – Acima: MASTER

from datetime import date

data_atual = date.today()
ano_atual = data_atual.year

ano_nas = int(input("Digite o ano de nascimento: "))

idade = ano_atual - ano_nas

if idade <= 9:
    print("Mirim")
elif idade <= 14:
    print("Infantil")
elif idade <= 19:
    print("Junior")
elif idade >= 20:
    print("Master")