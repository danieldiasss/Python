# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:

# A) quantas pessoas têm mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres têm menos de 20 anos.

print("="*30)
print("Cadastre alguém")
print("="*30)

homens = idade = maior_idade = mulheres_menor_20 = 0

while True:
    idade = int(input("Qual a idade? "))
    sexo = " "
    continuar = " "
    while sexo not in "MF":
        sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]
    while continuar not in "SN":
        continuar = str(input("Deseja continuar?[S/N]")).strip().upper()[0]
    
    if idade >18:
        maior_idade += 1

    elif idade <20 and sexo == "F":
        mulheres_menor_20 += 1

    if sexo == "M":
        homens += 1

    if continuar == "N":
        break

print("="*50)
print(f'''
O total de pessoas com mais de 18 anos foram {maior_idade}
O total de homens cadastrados foram {homens}.
O total de mulheres com menos de 20 anos foram {mulheres_menor_20}
''')
print("="*50)