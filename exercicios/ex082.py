# Crie um programa que vai ler vários números e colocar em uma lista.

# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.

# Ao final, mostre o conteúdo das três listas geradas.

lista1 = []  # todos
lista2 = []  # par
lista3 = []  # ímpar
while True:
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        lista1.append(num)
        lista2.append(num)
    else:
        lista1.append(num)
        lista3.append(num)
    continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if continuar == "N":
        break
    
print(f"A lista toda é {lista1}")
print(f"A lista somente ímpar é {lista3}")
print(f"A lista somente par é {lista2}")