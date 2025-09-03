# Faça um programa que leia o nome completo de uma pessoa e mostre em seguida o primeiro e ultimo nome
# Ex: Daniel Dias Ribeiro    ,   Daniel Ribeiro

n = str(input("Digite o seu nome completo: ")).strip()
nome = n.split()
print("Seu primeiro nome é {}" .format(nome[0]))
print("Seu último nome é {}" .format(nome[-1]))