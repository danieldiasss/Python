# Cria um programa que vai ler vários números e colocar em uma lista.

# Depois disso, mostre:

# A) Quantos números foram digitados.

# B) A lista de valores, ordenada de forma decrescente.

# C) Se o valor 5 foi digitado e está ou não na lista.

lista_numeros = []
continuar = ""
cont = 0
while continuar != "N":
    numeros =  int(input("Digite um número: "))
    continuar = str(input("Deseja continuar? [S/N]")).strip().upper()[0]
    cont+=1
    lista_numeros.append(numeros)
    lista_numeros.sort(reverse=True)
    
print(f"Foram digitados {cont} números")
print(f"A lista de valores de forma decrescente é {lista_numeros}")
if 5 in lista_numeros:
    print(f"O número 5 foi digitado")
else:
    print(f"O número 5 não foi digitado")
print("ENCERROU")