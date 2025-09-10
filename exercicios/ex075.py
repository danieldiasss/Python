# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

cont = 0
numeros = []
pares = []
while cont != 4:
    num = int(input("Digite um número:"))
    cont+= 1
    numeros.append(num)

    if 3 in numeros:
        posicao3 = numeros.index(3)
    else:
        posicao3 = None

    if num % 2 == 0:
        pares.append(num)
    
    

print(f' Os numeros escolhidos foram {numeros}x')
print(f'O valor 9 apareceu {numeros.count(9)}')
print(f'O 3 apareceu na posição {posicao3 +1}')
print(f'Os pares são {pares}')