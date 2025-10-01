# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. 
# No final, mostre:

# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

continuar = ''
pessoas = []
cont = 0
while continuar != "N":
    nome = str(input("Digite o nome: "))
    peso = float(input("Digite o peso: "))
    continuar = str(input("Deseja continuar? [S/N]")).strip().upper()
    cont+= 1

print(f'No total foram cadastradas {cont} pessoas')
pesos = [p[1] for p in pessoas]
maior = max(pesos)
menor = min(pesos)

mais_pesadas = [p[0] for p in pessoas if p[1] == maior]
mais_leves = [p[0] for p in pessoas if p[1] == menor]


print(f"O maior peso foi {maior}Kg. Peso de {mais_pesadas}")
print(f"O menor peso foi {menor}Kg. Peso de {mais_leves}")