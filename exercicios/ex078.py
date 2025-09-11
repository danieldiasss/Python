# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.

# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []
cont = 0
while cont < 5:
    num = int(input("Digite um número:"))
    lista.append(num)
    cont+= 1

menor = min(lista)
maior = max(lista)

print(f"Os valores escolhidos foram {lista}")
print(f"O menor valor é {menor} na posição", end = ' ')
for i,valor in enumerate(lista):
    if valor == menor:
        print(f"{i +1}",end='')

print()
print(f"O maior valor é {maior} na posição", end = ' ')
for i,valor in enumerate(lista):
    if valor == maior:
        print(f"{i + 1}",end='')