# Crie um programa que leia o nome completo de uma pessoa e motre:
# O nome com todas as letras maiúsculas
# O nome com todas as minúsculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome

nome = str(input("Digite seu nome completo: "))
nomeMA = nome.upper()
nomeMI = nome.lower()
letras = len(nome.replace(" ",""))
fname =  len(nome.split()[0])

print (f"""Seu nome em maiúsculas é {nomeMA}
Em minúsculas é {nomeMI}, possui
{letras} letras, e seu primeiro nome tem
{fname} letras. """)