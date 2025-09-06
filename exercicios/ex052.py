# Faça um programa que leia um número inteiro e diga se ele é ou não número primo
n = int(input("Digite um número: "))
cprimo = 0

for c in range (2,n):
    if n % c == 0:
        print(f"O número {n} é divisível por {c}")
        cprimo +=1
if cprimo > 2:
    print("Esse número não é primo")
else:
    print("Esse número é primo")