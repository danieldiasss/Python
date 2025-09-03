# Faça um programa que leia um ano qualquer e mostre se ele é bissexto
ano = int(input("Digite um ano: "))
if ano % 4 == 0:
    print("Esse ano é bissexto")
else:
    print("Esse ano não é bissexto")

# print("Esse ano é bissexto" if ano % 4 == 0 else "Esse ano não é bissexto") # forma de resolver por condição simplificada