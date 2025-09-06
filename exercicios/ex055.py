# Crie um programa que leia o peso de 5 pessoas e mostre o maior e menor peso
maior = 0
menor = 0
for c in range (1,6):
    peso = float(input(f"Digite o peso da {c}º pessoa: "))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f"O maior peso é {maior}kg e menor peso é {menor}kg")