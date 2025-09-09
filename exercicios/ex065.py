# Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

print("LEITOR DE NÚMEROS")
print("-=-"*30)

maior = menor = soma_idade = cont = 0
continuar = ""
while continuar != "N":
    num = float(input("Digite um número: "))

    cont += 1
    soma_idade += num
    media = soma_idade/cont
    
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    continuar = str(input("Deseja continuar? [S/N]")).upper().strip()[0]

print(f''' 
A média dos números deu {media}
O maior número é {maior}
O menor número é {menor}
''')

