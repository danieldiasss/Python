# Desenvolva um programa que leia o nome,idade e sexo de 4 pessoas. No final do programa mostre:
# A média de idade
# Qual é o nome do homem mais velho
# Quantas mulheres têm menos de 20 anos.
somaidade = 0
homem_mais_velho = 0
mulheres_menos_vinteanos = 0

for c in range (1,5):
    print(F"-------- {c}º pessoa: --------" )

    #nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo M/F: ")).upper()

    somaidade += idade
    media = somaidade/4

    if sexo == "M":
        if idade > homem_mais_velho:
            homem_mais_velho = idade
    if sexo == "F":
        if idade < 20:
            mulheres_menos_vinteanos += 1

       
print("------------------------------")
print(f"A média das idades é: {media}")
print(f"O homem mais velho é {homem_mais_velho}")
print(f"Existem {mulheres_menos_vinteanos} mulheres com menos de 20 anos.")