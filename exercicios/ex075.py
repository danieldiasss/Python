# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

cont = 0
numeros = []
pares = []
posicao_tres = 0

while cont != 4:
    num = int(input("Digite um número:"))
    cont+= 1
    numeros.append(num)

    if 3 in numeros:
        posicao_tres = numeros.index(3)

    if num % 2 == 0:
        pares.append(num)

print(f' Os numeros escolhidos foram {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O 3 apareceu na posição {posicao_tres}+1 ')
else:
    print("O valor 3 não foi digitado")
print(f'Os pares são {pares}')